def meu_assert(condicao, mensagem=None):
    if condicao:
        print('.', end='')
    else:
        # Pega a última chamada antes de `meu_assert`
        tb = traceback.extract_stack()[-2]
        erro = f'File "{tb.filename}", line {tb.lineno}, in {tb.name} >> {tb.line} >> AssertionError: {mensagem}'
        print(erro, end="")

def print_origem(origem, e):
    print(f"[🛑 Erro: {e}", end='|')
    print(f"📄 Linha {origem.lineno} no arquivo '{origem.filename}', função '{origem.name}':", end='|')
    print(f"🔧 Código que falhou: {origem.line}]", end="")

def test_date(value,expected):
    date = util.new_date(value) 
    expected = expected
    meu_assert (util.mesma_data(date, expected))


def meu_assertx(afirmacao, mensagem=""):
    try:
        assert afirmacao, mensagem
        print('.', end="")
    except AssertionError as e:
        tb = traceback.extract_tb(e.__traceback__)
        tb = traceback.extract_stack()[-2]

        # Se a stack trace tiver mais de 1 frame, tente pegar a origem correta
        if len(tb) > 1:
            # Pega o frame mais próximo de 'meu_assert' que não seja ele mesmo
            origem = next((frame for frame in reversed(tb) if frame.name != "meu_assert"), tb[0])
        else:
            origem = tb[0]  # No caso de erro direto em 'meu_assert', usa o próprio frame

        print_origem(origem, e)

        # raise  # Opcional: relança a exceção para interromper a execução

def meu_assert2(afirmacao, mensagem="",profundidade=-1):
    assert afirmacao, mensagem
    
    try:
        assert afirmacao, mensagem
        print('.',end="")
    except AssertionError as e:
        print('x',end="")

