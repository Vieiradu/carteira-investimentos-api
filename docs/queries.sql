
--Conta linhas de carteira_ativo agrupando por tipo
SELECT tipo, COUNT(*)
FROM carteira_ativo
GROUP BY tipo;

--Total investido por usuário → JOIN transacao+auth_user, SUM(quantidade * preco_unitario), GROUP BY usuário (decide se filtra tipo='COMPRA')
SELECT u.username, SUM(quantidade * preco_unitario) AS total_investido
FROM carteira_transacao AS t
INNER JOIN auth_user AS u ON t.usuario_id = u.id
WHERE t.tipo = 'COMPRA'
GROUP BY u.username;

--Transações com JOIN → transacao JOIN ativo (e opcional auth_user) mostrando o ticker
SELECT a.ticker, t.tipo, t.quantidade
FROM carteira_transacao AS t
JOIN carteira_ativo AS a ON t.ativo_id = a.id;