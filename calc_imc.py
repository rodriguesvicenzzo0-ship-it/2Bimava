#---lorran elias da conceição---
# Função: calcular_imc(p,a)
#Recebe peso (p) e altura (a), retorna o resultado da conta: peso/altura²
def calcular_imc(p,a):
    resultado = p/ (a ** 2)
    return resultado
#Davi2: classificador de dados
def classificar(valor_IMC)
   if <=25
      return "normal"
    else:
      return "acima do peso"
#Willian3: Especialista em conteúdo
def gerar_aviso(status):
 if status == "normal":
    return("Parabéns! Seu peso está adequando para sua altura! Mantenha os hábitos saúdaveis, com alimentação saudável e praticando atividades físicas")
 else:
    return("Seu IMC indica que você está acima do peso! Recomenda-se buscar uma dieta balenceada e incluir exercícios físicos em sua rotina")
# =====================================================================
#vicenzzo4 (Engenheiro de Integração)
# =====================================================================
# from logica import calcular_imc
# from classificacao import classificar
# from conteudo import gerar_aviso

def fluxo_principal():
    print("=== INICIANDO SISTEMA DE ANÁLISE DE IMC ===")
    
    try:
        peso = float(input("Digite o seu peso (em kg): "))
        altura = float(input("Digite a sua altura (em metros): "))
        imc_calculado = calcular_imc(peso, altura) 
        status_peso = classificar(imc_calculado)
        dica_saude = gerar_aviso(status_peso)
        
        print("\n-------------------------------------------")
        print(f"-> Seu IMC é: {imc_calculado:.2f}")
        print(f"-> Diagnóstico: {status_peso}")
        print(f"-> Recomendação: {dica_saude}")
        print("---------------------------------------------")
        
    except ValueError:
        print("\n[ERRO] Por favor, digite números válidos usando ponto (.) para decimais.")
if __name__ == "__main__":
    fluxo_principal():
