# Back-end Python and PostgreSQL

# Do Erro à Solução: O Guia Definitivo para Instalar Python com `pyenv` no Ubuntu 24.04

Ferramentas como o `pyenv` são fantásticas para gerenciar múltiplas versões do Python em um mesmo ambiente. No entanto, ao configurar uma nova máquina, especialmente com uma versão recente como o Ubuntu 24.04, podemos nos deparar com uma série de erros enigmáticos.

Este guia é um passo a passo prático, nascido de uma sessão real de troubleshooting, para transformar a frustração em aprendizado e deixar seu ambiente de desenvolvimento Python perfeitamente configurado.

## O Ponto de Partida: O Erro de SSL

Você decide instalar uma nova versão do Python com o `pyenv`, talvez a `3.11.6`. O comando `pyenv install 3.11.6` parece funcionar, mas ao tentar usar o `pip` para instalar qualquer pacote, você se depara com este erro assustador:

**O Erro:**
```text
WARNING: pip is configured with locations that require TLS/SSL...
SSLError("Can't connect to HTTPS URL because the SSL module is not available.")
````

**Diagnóstico:** Esta mensagem é clara: sua recém-instalada versão do Python não consegue estabelecer conexões seguras (HTTPS). Isso acontece porque, durante a compilação, o `pyenv` não encontrou as bibliotecas de desenvolvimento do OpenSSL no seu sistema.

**A Solução:** Precisamos instalar todas as dependências necessárias para a compilação completa do Python e, em seguida, reinstalar a versão desejada.

**Os Comandos:**

```bash
# Primeiro, instale todas as bibliotecas de desenvolvimento necessárias
sudo apt update && sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# Depois, remova a instalação incompleta do Python
pyenv uninstall 3.11.6

# E finalmente, instale-a novamente, agora com as dependências corretas
pyenv install 3.11.6
```

## Um Momento para Entender: O Python do Sistema vs. o Seu Python

Antes de prosseguir, é crucial entender um conceito fundamental. Ao explorar seu novo sistema Ubuntu, você pode notar que ele já vem com uma versão do Python instalada (no caso do 24.04, a versão `3.12`). Por que, então, todo esse trabalho para instalar outra?

**O Python do Sistema: O Coração do Ubuntu**
Pense no Python `3.12` nativo como uma **ferramenta interna do próprio sistema operacional**. O Ubuntu depende dele para executar scripts essenciais, gerenciar pacotes e rodar aplicações do sistema. Ele é instalado e meticulosamente gerenciado pelo `apt` (o gerenciador de pacotes do sistema) para garantir estabilidade e compatibilidade.

**O Perigo de Mexer no que Está Quieto**
Modificar o Python do sistema é uma receita para o desastre. Se você usasse o `pip` para instalar um pacote globalmente (`sudo pip install ...`), poderia, sem querer, atualizar uma biblioteca que uma ferramenta do sistema espera que esteja em uma versão mais antiga. Isso cria um "inferno de dependências" que pode quebrar partes críticas do seu Ubuntu. Foi exatamente por isso que os desenvolvedores do Debian e Ubuntu criaram a proteção `externally-managed-environment`, que veremos mais adiante.

**`pyenv`: A Sua Caixa de Ferramentas Particular**
É aqui que o `pyenv` brilha. Cada versão do Python que você instala com ele é criada em um **ambiente totalmente isolado e independente**, como um laboratório particular. Você tem total liberdade para instalar, atualizar e remover pacotes sem qualquer risco de interferir com o sistema operacional. O Python do sistema permanece intacto e funcional, e você tem um ambiente limpo e controlado para cada um dos seus projetos.

Agora que entendemos a importância de trabalhar em nosso ambiente `pyenv` isolado, vamos continuar nossa jornada de instalação...

## A Próxima Barreira: A Falha de Download

Com as dependências instaladas, você tenta reinstalar o Python, mas outro erro surge no caminho, desta vez relacionado à rede.

**O Erro:**

```text
Downloading Python-3.11.6.tar.xz...
error: failed to download Python-3.11.6.tar.xz
...
curl: (56) Recv failure: Conexão fechada pela outra ponta
```

**Diagnóstico:** O comando `curl`, usado pelo `pyenv` para baixar o código-fonte do Python, teve sua conexão interrompida. Isso pode ser uma instabilidade momentânea na sua rede, um firewall ou qualquer outro bloqueio de conexão.

**A Solução:** Se o problema for de rede, vamos contorná-lo\! Faremos o download do arquivo manualmente e o colocaremos no "cache" do `pyenv`. Assim, ele usará nosso arquivo local em vez de tentar baixá-lo novamente.

**Os Comandos:**

```bash
# 1. Baixe o arquivo manualmente para a pasta Downloads
wget [https://www.python.org/ftp/python/3.11.6/Python-3.11.6.tar.xz](https://www.python.org/ftp/python/3.11.6/Python-3.11.6.tar.xz) -P ~/Downloads/

# 2. Crie o diretório de cache do pyenv (se ele não existir)
mkdir -p ~/.pyenv/cache

# 3. Mova o arquivo baixado para o cache
mv ~/Downloads/Python-3.11.6.tar.xz ~/.pyenv/cache/

# 4. Tente a instalação novamente. Desta vez, ela pulará o download!
pyenv install 3.11.6
```

## O Guardião do Sistema: O Ambiente Gerenciado Externamente

Vitória\! O Python foi instalado com sucesso. Você sente a confiança voltar e executa o primeiro comando `pip`: `pip install --upgrade pip`. E então... mais um erro.

**O Erro:**

```text
error: externally-managed-environment
× This environment is externally managed
╰─> To install Python packages system-wide, try apt install...
```

**Diagnóstico:** Este não é um erro de falha, mas sim de **proteção**. Como discutimos, o Ubuntu 24.04 está te avisando que você está tentando modificar o Python do **sistema operacional**. Isso significa que seu terminal, por padrão, ainda está usando o Python nativo (`/usr/bin/python`) em vez do Python que acabamos de instalar com o `pyenv`.

**A Solução:** Precisamos configurar nosso terminal (shell) para que ele "saiba" que deve dar prioridade às versões do `pyenv`.

**Os Comandos:**

```bash
# 1. Defina a versão do pyenv como a padrão global para seu usuário
pyenv global 3.11.6

# 2. Adicione a configuração de inicialização do pyenv ao seu shell.
# O comando abaixo adiciona as linhas necessárias ao final do seu ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# 3. FECHE E ABRA SEU TERMINAL para que as mudanças façam efeito!
# Após reabrir, verifique se o pip correto está sendo usado:
which pip

# A saída deve ser: /home/seu-usuario/.pyenv/shims/pip

# 4. Agora sim, execute o comando do pip com segurança!
pip install --upgrade pip
```

## Conclusão

Passar por esses três erros pode parecer uma jornada árdua, mas cada um deles nos ensina uma lição valiosa sobre como nosso ambiente de desenvolvimento funciona: a importância das dependências de compilação, a realidade das falhas de rede e, mais importante, a diferença crucial entre o Python do sistema e o nosso ambiente de desenvolvimento isolado.

Agora você não só resolveu o problema, mas também compreendeu as causas, tornando-se um desenvolvedor mais preparado. Bom trabalho e bons códigos\!

## OBS

Podemos resolver esse problema de outra forma, CTRL + Shif + p digite "Select Interpreter", 
selecione "python,defaultInterpreterPath", isso vai configurar o VSCode para usar o caminho, 
"/bin/python3" onde está os arquivos binários do python, após isso ele vai pedir para configurar
o ambiente virtual do python, que no caso seria o que você configurou com "python -m venv .venv".