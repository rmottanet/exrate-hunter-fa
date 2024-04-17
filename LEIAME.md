# exRate Hunter

exRate Hunter é uma aplicação Python FastAPI desenvolvida como parte do projeto CoinSnark. Sua principal responsabilidade é fornecer dados atualizados para outras APIs dentro do projeto [CoinSnark](https://rmottanet.github.io/coinsnark), permitindo que elas consumam os dados do Redis sem a necessidade de atualizá-lo.

## Responsabilidade

A aplicação tem como responsabilidade consumir dados de várias fontes externas, como o Banco Central do Brasil (BCB), Open Exchange Rates e Exchange Rates API. Esses serviços fornecem dados financeiros relevantes, como taxas de câmbio.

Após a obtenção dos dados, a aplicação os consolida de acordo com a lógica de negócios específica do projeto CoinSnark. Em seguida, os dados consolidados são escritos no Redis, um armazenamento de dados em memória, para acesso rápido por outras partes do projeto.


Para obter mais informações sobre o projeto CoinSnark, consulte a documentação: [GitBook do Coinsnark](https://rmottanet.gitbook.io/coinsnark).


Agradeço por explorar o exRate Hunter. Caso tenha alguma dúvida ou sugestão sobre o projeto, fico felizes em ouvir. Sinta-se à vontade para entrar em contato.

<br />
<br />
<p align="center">
<a href="https://gitlab.com/rmottanet"><img src="https://img.shields.io/badge/Gitlab--_.svg?style=social&logo=gitlab" alt="GitLab"></a>
<a href="https://github.com/rmottanet"><img src="https://img.shields.io/badge/Github--_.svg?style=social&logo=github" alt="GitHub"></a>
<a href="https://instagram.com/rmottanet/"><img src="https://img.shields.io/badge/Instagram--_.svg?style=social&logo=instagram" alt="Instagram"></a>
<a href="https://www.linkedin.com/in/rmottanet/"><img src="https://img.shields.io/badge/Linkedin--_.svg?style=social&logo=linkedin" alt="Linkedin"></a>
</p>
<br />
