# Urubu do Pix
![image](https://github.com/victorthecreative/urubu_do_pix/assets/50841013/0a329e44-276b-4d75-bd18-20f456a20d74)

## Descrição

O projeto "Urubu do Pix" tem como objetivo treinar habilidades de desenvolvimento em Python, com foco em Orientação a Objetos, princípios de Clean Code e aplicação de conceitos da Clean Architecture. Este projeto é puramente educativo e não tem a intenção de ser usado para práticas ilícitas.

**Nota:** O nome "Urubu do Pix" faz referência a um golpe online, mas este projeto não tem nenhuma relação com atividades criminosas.

![Arquitetura do Projeto](https://github.com/victorthecreative/urubu_do_pix/assets/50841013/66da086b-3d40-4d63-9d65-a76b1f588a1d)

## Funcionalidades

1. **Cadastro de Usuários:** 
   - Permite o cadastro de novos usuários.
   - Gera automaticamente uma chave única para cada usuário.

2. **Realização de Depósitos:** 
   - Os usuários podem fazer depósitos.
   - O valor mínimo para depósito é de R$200.

3. **Cálculo de Rendimentos:** 
   - Calcula rendimentos diários com base em uma taxa de juros fixa.

## Arquitetura

O projeto segue os princípios da Clean Architecture, com as seguintes características:

- **Separation of Concerns:** A aplicação é dividida em diferentes módulos, cada um com sua responsabilidade específica.
- **Camadas de Abstração:** Há uma clara separação entre as camadas de interação com o banco de dados e as camadas de interação com o usuário.
- **Inversão de Dependência:** Utiliza funções e classes para abstrair a interação com o banco de dados.
- **Uso de Interfaces:** Modela objetos de domínio com comportamentos específicos.
- **Separação de Lógica de Negócios:** A lógica de negócios está encapsulada em classes específicas.

## Banco de Dados

O sistema utiliza 3 tabelas principais:
- **Usuários:** Armazena informações dos usuários.
- **Depósito:** Registra todos os depósitos feitos pelos usuários.
- **Rendimento:** Controla os rendimentos diários com base nos depósitos.
![Untitled](https://github.com/victorthecreative/urubu_do_pix/assets/50841013/4d06c4b8-1c81-4b87-ab4e-035fd866cd81)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar pull requests para melhorias.

## Autor

Victor Coelho

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

   
