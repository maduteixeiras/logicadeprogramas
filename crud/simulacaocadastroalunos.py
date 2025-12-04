
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import sqlite3
from datetime import datetime, timedelta
import threading
import time


# cor do programa
COR_FUNDO = "#00bfff"   # deepskyblue
COR_BOTAO = "#000080"   # navy (azul escuro)
COR_TEXTO = "#ffffff"   # branco

# banco de dados local 
# armazenando nome, curso, cpf, nascimento, endereço e alguma observação
def inicializar_banco(): 
    conn = sqlite3.connect("Cadastro_alunos.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cadastros (
            ra INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL, 
            cpf TEXT NOT NULL,
            nascimento TEXT NOT NULL,
            curso TEXT NOT NULL,
            endereco TEXT NOT NULL,
            observacoes TEXT
        )
    """)
    conn.commit()
    conn.close() 

def limpar_campos(): 
    entrada_nome.delete(0, tk.END)
    entrada_nascimento.set_date(datetime.now())
    entrada_cpf.delete(0, tk.END)
    entrada_curso.set("")
    entrada_endereco.delete("1.0", tk.END)
    entrada_observacoes.delete("1.0", tk.END)

def adicionar_aluno():
    nome = entrada_nome.get() #obrigratório informar
    nascimento = entrada_nascimento.get_date().strftime("%d/%m/%Y") #obrigatório informar
    curso = entrada_curso.get() #obrigatório informar
    endereco = entrada_endereco.get("1.0", tk.END).strip() #obrigatorio informar
    observacoes = entrada_observacoes.get("1.0", tk.END).strip() #opcional

    if not (nome and nascimento and curso and endereco): 
        messagebox.showerror("Prencha os campos corretamente!")
        return
    
    try:
        datetime.strptime(nascimento, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Erro ao verificar nascimento")
        return

    conn = sqlite3.connect("Cadastro_alunos.db") # pega as informações e armazena no banco de dados
    cur = conn.cursor() 
    cur.execute("""
        INSERT INTO cadastros 
        (nome, nascimento, curso, endereco, observacoes)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, nascimento, curso , observacoes))
    conn.commit()
    conn.close()
    carregar_cadastros()
    limpar_campos() # perimitindo excluir agendamento

# Carregar cadastros para mostrar na tabela
def carregar_cadastros():
    for item in tabela.get_children():
        tabela.delete(item)
    conn = sqlite3.connect("Cadastro_alunos.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cadastros ORDER BY ra")
    for row in cur.fetchall():
        tabela.insert("", tk.END, values=row)
    conn.close()

# Edição do cadastro
def editar_cadastro():
    item = tabela.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecione um agendamento para editar.")
        return
    # Pegar dados existentes
    dados = tabela.item(item)
    valores = dados['values']
    ag_ra = valores[0]

   # Preencher campos com dados existentes
    entrada_nome.delete(0, tk.END); entrada_nome.insert(0, valores[1])
    entrada_cpf.delete(0, tk.END); entrada_nome.insert(0, valores[1])
    # converter data/hora
    dia, mes, ano = valores[2].split('/')
    entrada_nascimento.set_date(datetime.strptime(valores[2], "%d/%m/%Y"))
    entrada_curso.set(valores[4])
    entrada_observacoes.delete("1.0", tk.END); entrada_observacoes.insert(tk.END, valores[6] or "")

    # Mudar funcionalidade do botão adicionar para salvar edição
    def salvar_edicao(): 
        nome2 = entrada_nome.get()
        cpf2 = entrada_cpf.get()
        nascimento2 = entrada_nascimento.get_date().strftime("%d/%m/%Y")
        curso2 = entrada_curso.get()
        observacoes2 = entrada_observacoes.get("1.0", tk.END).strip()

        if not(nome2 and nascimento2 and cpf2 and curso2 and observacoes2):
            messagebox.showerror("Erro", "Preencha os campos obrigatórios.")
            return
        try:
            datetime.strptime(nascimento2, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Erro", "Formato de aniversário inválido!")
            return
        
        conn2 = sqlite3.connect("Cadastro_alunos.db")
        cur2 = conn2.cursor()
        cur2.execute("""
            UPDATE cadastros
            SET nome=?, cpf= ?, nascimento=?, curso=?, observacoes=? 
            WHERE ra=?
        """, (nome2, cpf2,  nascimento2, curso2, observacoes2, ag_ra))
        conn2.commit()
        conn2.close()
        carregar_cadastros()
        limpar_campos()
        botao_adicionar.config(text="Adicionar cadastro", command=adicionar_aluno)

    botao_adicionar.config(text="Salvar Edição", command=salvar_edicao)

#layout de interface 
inicializar_banco()
janela = tk.Tk()
janela.title("Simulação de Cadastro de ALunos")
janela.geometry("900x700")
janela.configure(bg=COR_FUNDO)

# Calendário para ver os dias
frame_cal = tk.Frame(janela, bg=COR_FUNDO)
frame_cal.pack(pady=10)

cal = Calendar(frame_cal, selectmode='day', date_pattern='dd/mm/yyyy', background="white", foreground="black")
cal.pack()

def mostrar_cadastros(event):
    cad_selecionado = cal.get_date()
    # filtrar agendamentos desse dia
    conn = sqlite3.connect("Cadastro_alunos.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cadastros WHERE data=?", (cad_selecionado,))
    rows = cur.fetchall()
    conn.close()
    # atualizar tabela
    for item in tabela.get_children():
        tabela.delete(item)
    for r in rows:
        tabela.insert("", tk.END, values=r)

cal.bind("<<CalendarSelected>>", mostrar_cadastros)


# Frame de entrada de dados
frame_entrada = tk.Frame(janela, bg=COR_FUNDO)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Nome do Aluno:", bg=COR_FUNDO).grid(row=0, column=0, sticky="e")
entrada_nome = tk.Entry(frame_entrada, width=30)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="CPF do Aluno:", bg=COR_FUNDO).grid(row=2, column=0, sticky="e")
entrada_cpf = tk.Entry(frame_entrada, width=30)
entrada_cpf.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Data de Nascimento:", bg=COR_FUNDO).grid(row=3, column=0, sticky="e")
entrada_nascimento = DateEntry(frame_entrada, width=28, background='white', date_pattern='dd/mm/yyyy')
entrada_nascimento.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text= "Curso: ", bg=COR_FUNDO).grid(row=4, column=0, sticky="e")
entrada_curso = ttk.Combobox(frame_entrada, width=28)
entrada_curso['values'] = ['Analise de Sistemas', 'Administração', 'Eletrotécnica', 'Eletromecânica', 'Construção Civíl', 'Logística']
entrada_curso.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Endereço do aluno:", bg=COR_FUNDO).grid(row=5, column=0, sticky="ne")
entrada_endereco = tk.Text(frame_entrada, width=30, height=3)
entrada_endereco.grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Observações do Cliente:", bg=COR_FUNDO).grid(row=6, column=0, sticky="ne")
entrada_observacoes = tk.Text(frame_entrada, width=30, height=3)
entrada_observacoes.grid(row=5, column=1, padx=5, pady=5)

# Botões adicionar
botao_adicionar = tk.Button(janela, text="Adicionar Cadastro", bg=COR_BOTAO, fg=COR_TEXTO, command=adicionar_aluno)
botao_adicionar.pack(pady=5)
# Botão de editar
botao_editar = tk.Button(janela, text="Editar Aluno Selecionado", bg="#ffa726", fg="white", command=editar_cadastro)
botao_editar.pack(pady=5)


# Tabela de exibição das informações
colunas = ("RA", "Nome","CPF",  "Nascimento", "Curso", "Observações")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")


for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=110, anchor="center")

tabela.pack(pady=10, fill="both", expand=True)

# Botão excluir
botao_deletar = tk.Button(janela, text="Deletar Aluno Selecionado", bg="red", fg="white", command=lambda: deletar_aluno())
botao_deletar.pack(pady=5)

# Função deletar
def deletar_aluno():
    sel = tabela.selection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecione um aluno para excluir.")
        return
    res = messagebox.askyesno("Confirmação", "Deseja realmente excluir?")
    if res:
        item = tabela.item(sel)
        ag_ra = item['values'][0]
        conn = sqlite3.connect("Cadastro_alunos.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM cadastros WHERE ra=?", (ag_ra,))
        conn.commit()
        conn.close()
        carregar_cadastros()

# Carregar todos inicialmente
carregar_cadastros()

janela.mainloop()
