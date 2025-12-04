import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import sqlite3
from datetime import datetime


# cor do programa
COR_FUNDO = "#FFC0CB"   # rosa
COR_BOTAO = "#FF1493"   # rosa claro
COR_TEXTO = "#ffffff"   # branco

# banco de dados local 
# armazenando ra, nome, cpf, nascimento, curso, endereco, observacoes
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
    entrada_cpf.delete(0, tk.END)
    entrada_nascimento.set_date(datetime.now())
    entrada_curso.set("")
    entrada_endereco.delete("1.0", tk.END)
    entrada_observacoes.delete("1.0", tk.END)

def adicionar_aluno():
    nome = entrada_nome.get() 
    cpf = entrada_cpf.get() # Necessário pegar o cpf
    nascimento = entrada_nascimento.get_date().strftime("%d/%m/%Y") 
    curso = entrada_curso.get() 
    endereco = entrada_endereco.get("1.0", tk.END).strip() 
    observacoes = entrada_observacoes.get("1.0", tk.END).strip() 

    # Validação 
    if not (nome and cpf and nascimento and curso and endereco): 
        messagebox.showerror("Erro de Preenchimento", "Por favor, preencha todos os campos obrigatórios (Nome, CPF, Data de Nascimento, Curso, Endereço).")
        return
    
    try:
        datetime.strptime(nascimento, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Erro de Formato", "Formato de data de nascimento inválido.")
        return

    conn = sqlite3.connect("Cadastro_alunos.db") 
    cur = conn.cursor() 
    cur.execute("""
        INSERT INTO cadastros 
        (nome, cpf, nascimento, curso, endereco, observacoes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, cpf, nascimento, curso, endereco, observacoes))
    conn.commit()
    conn.close()
    carregar_cadastros()
    limpar_campos() 

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
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um aluno para editar.")
        return
    
    # Pegar dados existentes
    dados = tabela.item(item_selecionado)
    valores = dados['values']
    ag_ra = valores[0]

    # Preencher campos com dados existentes

    entrada_nome.delete(0, tk.END); entrada_nome.insert(0, valores[1])
    entrada_cpf.delete(0, tk.END); entrada_cpf.insert(0, valores[2]) # Usar entrada_cpf
    
    # Converter data/hora para preencher o DateEntry
    try:
        data_nasc = datetime.strptime(valores[3], "%d/%m/%Y")
        entrada_nascimento.set_date(data_nasc)
    except ValueError:
        messagebox.showerror("Erro", "Formato de data de nascimento no banco inválido.")
        return

    entrada_curso.set(valores[4])
    entrada_endereco.delete("1.0", tk.END); entrada_endereco.insert(tk.END, valores[5] or "") # Incluindo endereço
    entrada_observacoes.delete("1.0", tk.END); entrada_observacoes.insert(tk.END, valores[6] or "")

    # Mudar funcionalidade do botão adicionar para salvar edição
    def salvar_edicao(): 
        nome2 = entrada_nome.get()
        cpf2 = entrada_cpf.get()
        nascimento2 = entrada_nascimento.get_date().strftime("%d/%m/%Y")
        curso2 = entrada_curso.get()
        endereco2 = entrada_endereco.get("1.0", tk.END).strip() # Incluindo endereço
        observacoes2 = entrada_observacoes.get("1.0", tk.END).strip()

        if not(nome2 and cpf2 and nascimento2 and curso2 and endereco2): # Validação
            messagebox.showerror("Erro", "Preencha os campos obrigatórios.")
            return
        
        try:
            datetime.strptime(nascimento2, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Erro", "Formato de aniversário inválido!")
            return
        
        conn2 = sqlite3.connect("Cadastro_alunos.db")
        cur2 = conn2.cursor()
        # CORREÇÃO: UPDATE agora inclui 'endereco' e a ordem está correta
        cur2.execute("""
            UPDATE cadastros
            SET nome=?, cpf=?, nascimento=?, curso=?, endereco=?, observacoes=? 
            WHERE ra=?
        """, (nome2, cpf2, nascimento2, curso2, endereco2, observacoes2, ag_ra))
        conn2.commit()
        conn2.close()
        carregar_cadastros()
        limpar_campos()
        # Volta a funcionalidade do botão para "Adicionar cadastro"
        botao_adicionar.config(text="Adicionar cadastro", command=adicionar_aluno)

    botao_adicionar.config(text="Salvar Edição", command=salvar_edicao)

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

# layout de interface 
inicializar_banco()
janela = tk.Tk()
janela.title("Simulação de Cadastro de ALunos")
janela.geometry("900x700")
janela.configure(bg=COR_FUNDO)


def mostrar_cadastros_por_nascimento(event):
    pass


# Frame de entrada de dados
frame_entrada = tk.Frame(janela, bg=COR_FUNDO)
frame_entrada.pack(pady=10)

tk.Label(frame_entrada, text="Nome do Aluno:", bg=COR_FUNDO).grid(row=0, column=0, sticky="e")
entrada_nome = tk.Entry(frame_entrada, width=30)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="CPF do Aluno:", bg=COR_FUNDO).grid(row=1, column=0, sticky="e") 
entrada_cpf = tk.Entry(frame_entrada, width=30)
entrada_cpf.grid(row=1, column=1, padx=5, pady=5) # CORREÇÃO: row=1

tk.Label(frame_entrada, text="Data de Nascimento:", bg=COR_FUNDO).grid(row=2, column=0, sticky="e") 
entrada_nascimento = DateEntry(frame_entrada, width=28, background='white', date_pattern='dd/mm/yyyy')
entrada_nascimento.grid(row=2, column=1, padx=5, pady=5) # CORREÇÃO: row=2

tk.Label(frame_entrada, text= "Curso: ", bg=COR_FUNDO).grid(row=3, column=0, sticky="e") 
entrada_curso = ttk.Combobox(frame_entrada, width=28)
entrada_curso['values'] = ['Analise de Sistemas', 'Administração', 'Eletrotécnica', 'Eletromecânica', 'Construção Civíl', 'Logística']
entrada_curso.grid(row=3, column=1, padx=5, pady=5) # CORREÇÃO: row=3

tk.Label(frame_entrada, text="Endereço do aluno:", bg=COR_FUNDO).grid(row=4, column=0, sticky="ne") 
entrada_endereco = tk.Text(frame_entrada, width=30, height=3)
entrada_endereco.grid(row=4, column=1, padx=5, pady=5) # CORREÇÃO: row=4

tk.Label(frame_entrada, text="Observações do Aluno:", bg=COR_FUNDO).grid(row=5, column=0, sticky="ne") 
entrada_observacoes = tk.Text(frame_entrada, width=30, height=3)
entrada_observacoes.grid(row=5, column=1, padx=5, pady=5) # CORREÇÃO: row=5


# Botões adicionar
botao_adicionar = tk.Button(janela, text="Adicionar Cadastro", bg=COR_BOTAO, fg=COR_TEXTO, command=adicionar_aluno)
botao_adicionar.pack(pady=5)
# Botão de editar
botao_editar = tk.Button(janela, text="Editar Aluno Selecionado", bg="#FF007F", fg="white", command=editar_cadastro)
botao_editar.pack(pady=5)


# Tabela para exibir 
colunas = ("RA", "Nome","CPF",  "Nascimento", "Curso", "Endereço", "Observações")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")


for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=100, anchor="center")

# Ajuste a largura de algumas colunas para caber o Endereço
tabela.column("Endereço", width=150, anchor="w")
tabela.column("Observações", width=150, anchor="w")


tabela.pack(pady=10, fill="both", expand=True)

# Botão excluir
botao_deletar = tk.Button(janela, text="Deletar Aluno Selecionado", bg="red", fg="white", command=deletar_aluno)
botao_deletar.pack(pady=5)

# Carregar todos inicialmente
carregar_cadastros()

janela.mainloop()