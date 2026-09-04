# Qualidade e segurança de sistemas de IA

Ao analisar IA, siga o caminho causal: dados de entrada → recuperação/contexto → composição de prompt → modelo → ferramentas → pós-processamento → persistência/telemetria.

## Qualidade

Defina tarefa, população de casos, baseline, métrica, limiar, intervalo de confiança quando aplicável, casos adversariais e regra GO/NO-GO. Separe qualidade do modelo, qualidade da recuperação, sucesso da tarefa e segurança.

## Segurança

Verifique autorização antes da recuperação, isolamento de tenant, minimização e redaction de dados, instruções não confiáveis, permissões de ferramentas, confirmação de ações de alto impacto, auditoria e contenção de loops/retries.

## Dados voláteis

Preços, quotas, disponibilidade, IDs de modelos, limites de contexto e comportamento de provedores devem ser tratados como desconhecidos até serem verificados na documentação oficial atual ou na configuração implantada.
