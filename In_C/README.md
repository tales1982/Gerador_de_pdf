# Gerador de PDF em C

Este projeto demonstra como criar um gerador de PDFs simples utilizando a linguagem C e a biblioteca **libharu**. O código permite gerar um PDF contendo texto formatado, e pode ser expandido para incluir imagens, gráficos e outros elementos.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em seu sistema:

- GCC (ou outro compilador C compatível)
- Biblioteca **libharu** (libhpdf)

### Instalação da libharu

Dependendo do seu sistema operacional, você pode instalar a libharu com os seguintes comandos:

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install libhpdf-dev
```

#### Fedora/Red Hat
```bash
sudo dnf install libharu-devel
```

#### macOS (usando Homebrew)
```bash
brew install libharu
```

## Compilação
Após instalar a libharu, você pode compilar o código C usando o GCC. Se a biblioteca estiver instalada em diretórios padrão, basta usar:

```bash
gcc gerador_pdf.c -o gerador_pdf -lhpdf
```