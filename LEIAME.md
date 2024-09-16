# exRate Hunter

exRate Hunter é uma aplicação Python FastAPI desenvolvida como parte do projeto CoinSnark. Sua principal responsabilidade é fornecer dados atualizados para outras APIs dentro do projeto [CoinSnark](https://rmottanet.github.io/coinsnark), permitindo que elas consumam os dados do Redis sem a necessidade de atualizá-lo.

## Responsabilidade

A aplicação tem como responsabilidade consumir dados de várias fontes externas, como o Banco Central do Brasil (BCB), Open Exchange Rates e Exchange Rates API. Esses serviços fornecem dados financeiros relevantes, como taxas de câmbio.

Após a obtenção dos dados, a aplicação os consolida de acordo com a lógica de negócios específica do projeto CoinSnark. Em seguida, os dados consolidados são escritos no Redis, um armazenamento de dados em memória, para acesso rápido por outras partes do projeto.

## Uso

Para utilizar o exRate Hunter, siga estas instruções:

1. Clone o repositório.
2. Instale as dependências listadas no arquivo `requirements.txt`.
3. Configure as variáveis de ambiente no arquivo `.env` renomeando o arquivo `.env-example`.
4. Execute o arquivo `main.py` para iniciar o servidor FastAPI.
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

Para obter mais informações sobre o projeto CoinSnark, consulte a documentação: [GitBook do Coinsnark](https://rmottanet.gitbook.io/coinsnark).

---

Agradeço por explorar o exRate Hunter. Caso tenha alguma dúvida ou sugestão sobre o projeto, fico felizes em ouvir. Sinta-se à vontade para entrar em contato.

<br />
<br />
<div align="center">
  <a href="https://bitbucket.org/rmottalabs/"><img alt="Static Badge" src="https://img.shields.io/badge/-Bitbucket?style=social&logo=bitbucket&logoSize=auto&label=Bitbucket&link=https%3A%2F%2Fbitbucket.org%2Frmottalabs%2Fworkspace%2Foverview%2F"></a>
  <a href="https://gitlab.com/rmottanet"><img alt="Static Badge" src="https://img.shields.io/badge/-Gitlab?style=social&logo=gitlab&logoSize=auto&label=Gitlab&link=https%3A%2F%2Fgitlab.com%2Frmottanet"></a>
  <a href="https://github.com/rmottanet"><img alt="Static Badge" src="https://img.shields.io/badge/-Github?style=social&logo=github&logoSize=auto&label=Github&link=https%3A%2F%2Fgithub.com%2Frmottanet"></a>
  <a href="https://hub.docker.com/"><img alt="Static Badge" src="https://img.shields.io/badge/-DockerHub?style=social&logo=docker&logoSize=auto&label=DockerHub&link=https%3A%2F%2Fhub.docker.com%2Fu%2Frmottanet"></a>
</div>
