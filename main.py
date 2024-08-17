
from fpdf import FPDF

# Create a PDF object
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_font("Arial", size = 12)
pdf.multi_cell(0, 10, txt="Contrato de Locação Comercial", align="C")

# Add the content
contract_text = """
Pelo presente instrumento particular, de um lado, como LOCADORA, NOME##### #######, CPF ###.###.###-## e, de outro lado, como LOCATÁRIA, NOME##########, RG ###########, inscrita no CPF ###.###.###-## domiciliada no endereço n° ##, ###################, resolvem celebrar o presente contrato de locação do imóvel situado no endereço Rua ###################, o qual reger-se-á pelas seguintes cláusulas e condições:

I. OBJETO:
Constitui objeto do presente contrato a locação do imóvel situado na Rua Antonino Fontes Mascarenhas N° 106, esquina com Rua Paulo VI, N° ###################, composto por 2 salas com aproximadamente 40 m² e um WC.

II. PRAZO:
O prazo de locação é de 12 meses, com a hipótese de renovação do contrato automaticamente, tendo início em ##/##/####. O pagamento será efetuado somente por transferência bancária.

BANCO DO ######
Conta Corrente
AGÊNCIA: #####
CONTA: #######-#
CPF: ###.###.###-##
NOME: ##### ## ##### ##########

Parágrafo Primeiro: Se a LOCATÁRIA, usando da faculdade que lhe confere o artigo 4º da Lei n.º 8.245 de 18 de outubro de 1991, devolver o imóvel locado antes do decorrido o prazo ajustado no caput desta cláusula, pagará à LOCADORA a multa compensatória correspondente a 03 (três) meses de aluguel em vigor, reduzida proporcionalmente ao tempo do contrato já cumprido, na forma do artigo 924 do Código Civil, na base de 1/12 (um doze avos) para cada mês já transcorrido.

Parágrafo Segundo: Findo o prazo acima ajustado, se a LOCATÁRIA continuar no imóvel por mais de 30 (trinta) dias, sem oposição da LOCADORA, a locação será prorrogada automaticamente por prazo indeterminado, nas mesmas bases contratuais; entretanto, o imóvel somente poderá ser retomado nos casos previstos em lei, mas poderá ser devolvido pela LOCATÁRIA a qualquer tempo, sem a incidência de qualquer multa por este motivo, desde que mediante comunicação prévia, por escrito, com antecedência mínima de 30 (trinta) dias da data da restituição do imóvel locado, sob pena de pagar a quantia correspondente a um mês de aluguel e encargos vigentes.

Parágrafo Terceiro: Após o recebimento de pedido por escrito da LOCATÁRIA, a LOCADORA terá o prazo de cinco dias para efetuar a vistoria do imóvel, correndo por conta da LOCATÁRIA o aluguel até a efetiva devolução do imóvel à LOCADORA.

III. FINALIDADE:
O imóvel é locado para uso exclusivamente comercial de uma loja destinada à venda de roupas, não podendo a locatária exercer outro ramo senão o aqui estipulado.

IV. PREÇO E FORMA DE PAGAMENTO:
O valor do aluguel mensal é de R$ 1.000,00 (Mil Reais), mais R$ 1.000,00 (Mil Reais) de garantia, sendo R$ 2.000,00 (Dois Mil Reais) para entrada no imóvel, seguido de R$ 1.000,00 (Mil Reais) de aluguel mensal nos primeiros 12 (doze) meses de locação, com vencimento todo dia 01 de cada mês. Ao fim desse prazo, o valor pode ser ajustado, mantendo o mesmo vencimento fixado acima.

Parágrafo Primeiro: O aluguel estabelecido no "caput" desta cláusula deverá ser pago em moeda corrente para a Locadora na data do vencimento, na conta bancária citada neste contrato.

V. ATRASO NO PAGAMENTO:
O não pagamento do aluguel no prazo ajustado na cláusula 4ª implicará em multa de 2% (dois por cento) sobre o valor do débito, juros de 1% (um por cento) ao mês e correção monetária calculada pelo IGPM da FGV.

VI. REAJUSTE DO ALUGUEL:
O aluguel pactuado na cláusula anterior sofrerá reajustes anuais com base na variação do Índice Geral de Preços divulgado pela Fundação Getúlio Vargas (IGP-FGV) ou outro índice que porventura venha a substituí-lo.

VII. USO DO IMÓVEL:
A locatária obriga-se a manter o imóvel locado em boas condições de higiene, limpeza e conservação, mantendo em perfeito estado as suas instalações elétricas e hidráulicas, a fim de restituí-lo no estado em que o recebeu, salvo as deteriorações decorrentes do uso normal.

VIII. BENFEITORIAS:
Eventuais reformas ou adaptações que a locatária pretender executar no imóvel, só poderão ser realizadas mediante autorização prévia e expressa da locadora.

IX. EXIGÊNCIAS DOS PODERES PÚBLICOS:
A locatária obriga-se a satisfazer todas as exigências dos poderes públicos a que der causa.

X. CESSÃO, SUBLOCAÇÃO E EMPRÉSTIMO:
A locatária não poderá transferir este contrato ou sublocar o imóvel, no todo ou em parte, sem prévia autorização por escrito da locadora.

XI. DESPESAS DE CONDOMÍNIO, CONSUMO E TAXAS:
Todas as despesas decorrentes da locação, quais sejam, consumo de água, luz, telefone, gás, prêmio de seguro contra incêndio, além do IPTU, ficam a cargo da locatária, cabendo-lhe efetuar diretamente esses pagamentos nas devidas épocas.

XII. VISTORIA:
A locatária desde já faculta à locadora examinar ou vistoriar o prédio sempre que esta entender conveniente, desde que previamente acordados dia e hora.

XIII. RESCISÃO:
O presente contrato ficará rescindido de pleno direito, independentemente de qualquer notificação judicial ou extrajudicial e sem que assista a nenhuma das partes o direito a qualquer indenização, ficando as partes, daí por diante, desobrigadas de todas as cláusulas deste contrato, nos seguintes casos: a) Processo de desapropriação total ou parcial do imóvel locado; b) Ocorrência de qualquer evento ou incêndio no imóvel locado que impeça a sua ocupação, havendo ou não culpa da locatária e dos que estão sob sua responsabilidade; ou c) Qualquer outro fato que obrigue o impedimento do imóvel locado, impossibilitando a continuidade da locação.

XIV. ALIENAÇÃO DO IMÓVEL:
Caso o imóvel objeto da locação seja alienado durante o prazo locatício, o adquirente fica obrigado a respeitar o presente contrato.

XV. SUBSTITUIÇÃO DA GARANTIA:
No caso de morte, falência ou insolvência do fiador, a locatária será obrigada, dentro de 30 (trinta) dias, a substituir a garantia locatícia.

XVI. INFRAÇÃO CONTRATUAL:
A parte que infringir o presente contrato pagará à parte inocente o valor correspondente a 3 (três) aluguéis vigentes à época da infração, sem prejuízo de arcar com eventuais perdas e danos que ocasionar e determinar a imediata rescisão do contrato.

E, por estarem, assim ajustados, assinam o presente contrato em 3 (três) vias, juntamente com duas testemunhas que a tudo assistiram, para que possa surtir seus efeitos legais.

Itamaraju (BA), 17/08/2024
"""
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, contract_text)

# Add the signature lines with proper alignment
pdf.ln(10)  # Add some space

# First row: Locadora and Locatária
pdf.cell(90, 10, "Locadora", 0, 0, "C")
pdf.cell(90, 10, "Locatária", 0, 1, "C")

pdf.cell(90, 10, "##### ######### #####", 0, 0, "C")
pdf.cell(90, 10, "##### ######### #####", 0, 1, "C")

pdf.cell(90, 10, "CPF: ###.###.###-##", 0, 0, "C")
pdf.cell(90, 10, "CPF: ###.###.###-##", 0, 1, "C")

pdf.cell(90, 20, "_____________________________", 0, 0, "C")
pdf.cell(90, 20, "_____________________________", 0, 1, "C")

# Add some space before the witness section
pdf.ln(10)

# Second row: Witnesses
pdf.cell(90, 10, "Testemunha 1", 0, 0, "C")
pdf.cell(90, 10, "Testemunha 2", 0, 1, "C")

pdf.cell(90, 10, "##### ######### #####", 0, 0, "C")
pdf.cell(90, 10, "##### ######### #####", 0, 1, "C")

pdf.cell(90, 10, "CPF: ###.###.###-##", 0, 0, "C")
pdf.cell(90, 10, "CPF: ###.###.###-##", 0, 1, "C")

pdf.cell(90, 20, "_____________________________", 0, 0, "C")
pdf.cell(90, 20, "_____________________________", 0, 1, "C")

# Save the pdf with the correct path
pdf_output_path = "/home/tales/Documents/Contrato_de_Locacao_Comercial.pdf"
pdf.output(pdf_output_path)