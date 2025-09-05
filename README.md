<!-- omit in toc -->
# Artífice ✨ - Um Estudo em Python e GUI

![preview_do_app](https://i.imgur.com/l6S2GeW.png)

<div align="center">

[![Status da Build](https://img.shields.io/github/actions/workflow/status/freitaseric/artifice/build-release.yml?branch=main&style=for-the-badge)](https://github.com/freitaseric/artifice/actions)
[![Último Commit](https://img.shields.io/github/last-commit/freitaseric/artifice?style=for-the-badge)](https://github.com/freitaseric/artifice/commits/main)
[![Issues Abertas](https://img.shields.io/github/issues/freitaseric/artifice?style=for-the-badge)](https://github.com/freitaseric/artifice/issues)
[![Licença](https://img.shields.io/github/license/freitaseric/artifice?style=for-the-badge)](https://github.com/freitaseric/artifice/blob/main/LICENSE)
[![Python Version](https://img.shields.io/python/required-version-toml?style=for-the-badge&tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Ffreitaseric%2Fartifice%2Fmain%2Fpyproject.toml)](https://www.python.org/downloads/)

</div>

<!-- omit in toc -->
## 📜 Sumário

- [🎯 Sobre o Projeto](#-sobre-o-projeto)
- [📚 Objetivos de Aprendizagem e Conceitos Explorados](#-objetivos-de-aprendizagem-e-conceitos-explorados)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [💾 Downloads e Instalação (Para Usuários)](#-downloads-e-instalação-para-usuários)
- [👨‍💻 Para Desenvolvedores (Rodando a partir do Código-Fonte)](#-para-desenvolvedores-rodando-a-partir-do-código-fonte)
- [📜 Licença](#-licença)


## 🎯 Sobre o Projeto

**Artífice** é um projeto de estudo criado para explorar o desenvolvimento de aplicações de desktop modernas com Python. O objetivo não era criar uma ferramenta de produção, mas sim aprender e aplicar conceitos de interfaces gráficas, manipulação de imagens e as melhores práticas do ecossistema Python atual.

A aplicação permite carregar uma imagem base, aplicar um logo pré-definido em coordenadas específicas e visualizar o resultado em tempo real antes de salvar a imagem final.

## 📚 Objetivos de Aprendizagem e Conceitos Explorados

Este projeto serviu como um playground para aprender sobre:

- **Setup de Projetos Modernos:** Utilização do `pyproject.toml` para uma gestão de dependências declarativa e reprodutível.
- **Ambientes Virtuais com `uv`:** Uso do `uv`, uma ferramenta de alta performance em Rust, para criar ambientes e instalar pacotes de forma extremamente rápida.
- **Qualidade de Código com `Ruff`:** Configuração de um linter e formatador integrado para garantir um código limpo e consistente com o mínimo de esforço.
- **Desenvolvimento de GUI com `CustomTkinter`:** Criação de uma interface gráfica bonita e responsiva, explorando a estrutura de widgets, frames e layouts em grid.
- **Manipulação de Imagens com `Pillow`:** Carregamento, composição (paste) com canais alfa (transparência) e salvamento de imagens em diferentes formatos.
- **Programação Orientada a Eventos:** Implementação de callbacks para botões e eventos de teclado (`<KeyRelease>`) para criar uma experiência interativa.
- **UI Reativa:** Desenvolvimento de uma função de preview que atualiza a interface em tempo real com base na entrada do usuário.

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **CustomTkinter:** Para a criação da interface gráfica.
- **Pillow (PIL):** Para toda a manipulação de imagens.
- **uv:** Gerenciador de pacotes e ambientes virtuais.
- **Ruff:** Linter e formatador de código.

## 💾 Downloads e Instalação (Para Usuários)

Para a sua conveniência, a aplicação é compilada automaticamente para Windows, macOS e Linux a cada nova atualização. Para baixar a versão mais recente, siga os passos:

1.  Vá para a aba **[Actions](https://github.com/freitaseric/artifice/actions)** deste repositório.
2.  Na lista de workflows à esquerda, clique em **"Build & Release Cross-Platform"**.
3.  Selecione a execução mais recente no topo da lista (deve ter um ícone de visto verde ✅).
4.  Na página de resumo, role para baixo até a seção **"Artifacts"**.
5.  Baixe o arquivo correspondente ao seu sistema operacional.

<!-- omit in toc -->
### Pós-Download:

- **Windows:**

  1.  Baixe o `Artifice-Windows-Installer.exe`.
  2.  Execute o instalador e siga as instruções.

- **macOS:**

  1.  Baixe o `Artifice-macOS.dmg`.
  2.  Abra o arquivo `.dmg`.
  3.  Arraste o ícone do `Artifice.app` para a sua pasta de `Aplicativos`.

- **Linux (AppImage):**
  1.  Baixe o `Artifice-Linux-AppImage`.
  2.  Dê permissão de execução ao arquivo. Pelo terminal:
      ```bash
      chmod +x Artifice-x86_64.AppImage
      ```
  3.  Execute o arquivo com um duplo clique ou pelo terminal: `./Artifice-x86_64.AppImage`.

## 👨‍💻 Para Desenvolvedores (Rodando a partir do Código-Fonte)

Se você deseja explorar o código, modificá-lo ou contribuir, siga os passos abaixo para configurar o ambiente de desenvolvimento.

Para rodar este projeto localmente e explorar o código, siga os passos abaixo.

<!-- omit in toc -->
### Pré-requisitos:

- Python 3.8 ou superior.
- [uv](https://github.com/astral-sh/uv) instalado no sistema.
- A biblioteca `tk` do Tcl/Tk.

<!-- omit in toc -->
### Passos:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/freitaseric/artifice.git
    cd artifice
    ```

2.  **Sincronize as dependências:**

    ```bash
    uv sync
    ```

<!-- omit in toc -->
### ▶️ Como Usar

Com as dependências instaladas, execute o seguinte comando no terminal:

```bash
uv run app.py
```

## 📜 Licença

Este projeto é distribuído sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. Sinta-se à vontade para usar este código como base para seus próprios estudos!
