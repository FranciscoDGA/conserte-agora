(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.ConserteDiagnostico = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /**
   * REGRAS E CONTEÚDO REVISADO DO DIAGNÓSTICO GUIADO (V1)
   * Tema de baixo risco: Fechadura ou maçaneta de porta com dificuldade
   * Fonte única do conteúdo: artigos/como-consertar-fechadura-de-porta.html (revisado em 21/11/2026)
   *
   * Como a equipe editorial revisa este arquivo:
   * - Todas as perguntas estão em `FLOW.questions` (cada opção aponta para `nextQuestion` ou `outcome`).
   * - Todos os resultados estão em `FLOW.outcomes`.
   * - Nenhum texto é gerado por IA em tempo real: o motor apenas exibe o resultado pré-aprovado.
   * - Todo resultado possui `safetyAlerts` (exibidos obrigatoriamente ANTES de qualquer orientação),
   *   `hypothesis` (sempre apresentado como hipótese/possibilidade, nunca certeza) e `actionType`
   *   ('guia_existente' | 'profissional' | 'informacao_insuficiente').
   */
  const FLOW = {
    id: 'fechadura-porta-v1',
    title: 'Diagnóstico Guiado: Fechadura ou Maçaneta de Porta',
    lastReviewed: '21 de novembro de 2026',
    reviewedBy: 'Equipe Editorial Conserte Agora',
    sourceGuide: {
      title: 'Como ajustar fechadura de porta: lubrificação, maçaneta frouxa e alinhamento básico',
      url: 'artigos/como-consertar-fechadura-de-porta.html'
    },
    toolsGuide: {
      title: '10 ferramentas básicas para ter em casa: como escolher e usar com segurança',
      url: 'artigos/10-ferramentas-essenciais-para-ter-em-casa.html'
    },
    initialSafetyNotice: [
      'Realize qualquer observação sempre com a porta aberta e escorada por um calço no chão, evitando ficar trancado.',
      'Não force chaves tortas ou trincadas e nunca desmonte a caixa interna da fechadura (ela contém molas sob tensão).'
    ],
    questions: {
      q1_triagem: {
        id: 'q1_triagem',
        stepNumber: 1,
        question: '1. Qual é a situação geral da porta e da fechadura neste momento?',
        helpText: 'Esta pergunta identifica situações que exigem parada imediata ou atendimento profissional.',
        options: [
          {
            id: 'opt_mecanica_comum',
            label: 'É uma fechadura mecânica comum (chave simples e maçaneta), sem chave quebrada lá dentro',
            nextQuestion: 'q2_teste_porta_aberta'
          },
          {
            id: 'opt_chave_quebrada_ou_entrada',
            label: 'A chave quebrou dentro do miolo, está trincada/torta, ou a porta principal de entrada corre risco de não trancar',
            outcome: 'out_profissional_chave_ou_seguranca'
          },
          {
            id: 'opt_fechadura_eletronica',
            label: 'É uma fechadura digital / eletrônica (com senha, biometria, cartão ou pilhas)',
            outcome: 'out_profissional_eletronica'
          },
          {
            id: 'opt_nao_sei_q1',
            label: 'Não tenho certeza sobre o tipo de fechadura ou condição da chave',
            outcome: 'out_informacao_insuficiente'
          }
        ]
      },
      q2_teste_porta_aberta: {
        id: 'q2_teste_porta_aberta',
        stepNumber: 2,
        question: '2. Com a porta totalmente ABERTA, o que acontece ao girar a chave e abaixar a maçaneta?',
        helpText: 'Testar com a porta aberta permite separar falhas da fechadura de problemas de alinhamento com o batente.',
        options: [
          {
            id: 'opt_aberta_funciona_fechada_nao',
            label: 'Com a porta aberta a chave e o trinco funcionam macios, mas com a porta fechada ela não tranca direito',
            nextQuestion: 'q3_alinhamento_dobradicas'
          },
          {
            id: 'opt_chave_agarrando_aberta',
            label: 'Mesmo com a porta aberta, a chave entra ou gira com dificuldade (parece seca ou agarrando)',
            outcome: 'out_hipotese_lubrificacao'
          },
          {
            id: 'opt_macaneta_frouxa',
            label: 'A maçaneta ou o espelho externo estão bambos/frouxos na mão, mas a lingueta ainda recolhe ao abaixar',
            outcome: 'out_hipotese_macaneta_frouxa'
          },
          {
            id: 'opt_mecanismo_solto',
            label: 'A maçaneta abaixa toda sem recolher a lingueta, ou a chave gira 360° em falso sem mover a tranca',
            outcome: 'out_profissional_mecanismo_interno'
          },
          {
            id: 'opt_nao_sei_q2',
            label: 'O comportamento é diferente desses ou não consegui observar com segurança',
            outcome: 'out_informacao_insuficiente'
          }
        ]
      },
      q3_alinhamento_dobradicas: {
        id: 'q3_alinhamento_dobradicas',
        stepNumber: 3,
        question: '3. Ao observar as dobradiças e a folha da porta, qual destes sinais você percebe?',
        helpText: 'Quando a fechadura funciona aberta mas trava fechada, a lingueta costuma estar batendo fora do furo do batente.',
        options: [
          {
            id: 'opt_parafusos_dobradica_frouxos',
            label: 'Os parafusos da dobradiça superior parecem levemente folgados, mas a madeira está íntegra',
            outcome: 'out_hipotese_desalinhamento_leve'
          },
          {
            id: 'opt_madeira_inchada_ou_espanada',
            label: 'A porta inchou/empenou, raspa bastante no chão/batente, ou os parafusos giram em falso na madeira esfarelada',
            outcome: 'out_profissional_marcenaria'
          },
          {
            id: 'opt_nao_sei_q3',
            label: 'Não consigo identificar se há folga nas dobradiças ou onde a lingueta encosta',
            outcome: 'out_informacao_insuficiente'
          }
        ]
      }
    },
    outcomes: {
      out_hipotese_lubrificacao: {
        id: 'out_hipotese_lubrificacao',
        actionType: 'guia_existente',
        badgeText: 'Hipótese de baixa complexidade • Guia disponível',
        title: 'Hipótese: possível atrito seco no cilindro (miolo da chave)',
        safetyAlerts: [
          'Mantenha a porta aberta e travada com um calço no chão durante toda a verificação.',
          'NÃO aplique óleo de cozinha, graxa ou óleo desengripante líquido dentro do buraco da chave (líquidos retêm poeira e formam uma borra que trava os pinos).',
          'Não force a chave com alicate e não abra a caixa interna da fechadura.'
        ],
        hypothesis: 'Como a chave agarra mesmo com a porta aberta, uma possibilidade comum é a falta de lubrificação a seco nos pinos internos do cilindro. Outra possibilidade é desgaste mecânico da própria chave ou do cilindro.',
        whatToDo: 'Consulte a Etapa 1 do nosso guia revisado para ver como aplicar apenas grafite em pó seco no cilindro e quando parar caso a chave continue prendendo.',
        guideSectionLabel: 'Ir para a Etapa 1: Lubrificar o cilindro com grafite em pó',
        guideUrl: 'artigos/como-consertar-fechadura-de-porta.html',
        whenToCallPro: 'Se mesmo após aplicar uma pequena dose de grafite em pó a chave continuar travando, pare de forçar e chame um chaveiro profissional para avaliar o cilindro.'
      },
      out_hipotese_macaneta_frouxa: {
        id: 'out_hipotese_macaneta_frouxa',
        actionType: 'guia_existente',
        badgeText: 'Hipótese de baixa complexidade • Guia disponível',
        title: 'Hipótese: possível folga no pino de fixação da maçaneta ou nos parafusos do espelho',
        safetyAlerts: [
          'Trabalhe exclusivamente com a porta aberta e escorada por um calço no chão, para que o trinco nunca feche com a maçaneta solta.',
          'Não desmonte a caixa interna embutida na madeira da porta (ela possui molas sob tensão).',
          'Use uma chave de fenda, Phillips ou Allen que encaixe sem folga na cabeça do parafuso.'
        ],
        hypothesis: 'Quando a lingueta ainda recolhe normalmente mas a maçaneta ou a placa externa balançam, uma hipótese frequente é o afrouxamento do pequeno parafuso lateral/inferior do pescoço da maçaneta ou dos parafusos externos do espelho.',
        whatToDo: 'Veja na Etapa 2 do nosso guia revisado como localizar e reapertar o pino de fixação da maçaneta e os parafusos do espelho externo.',
        guideSectionLabel: 'Ir para a Etapa 2: Reapertar maçanetas e espelhos frouxos',
        guideUrl: 'artigos/como-consertar-fechadura-de-porta.html',
        whenToCallPro: 'Se o eixo quadrado central estiver torto/quebrado ou se os parafusos girarem em falso na madeira espanada, interrompa o ajuste e acione um chaveiro ou marceneiro.'
      },
      out_hipotese_desalinhamento_leve: {
        id: 'out_hipotese_desalinhamento_leve',
        actionType: 'guia_existente',
        badgeText: 'Hipótese de baixa complexidade • Guia disponível',
        title: 'Hipótese: possível desalinhamento leve por folga na dobradiça superior',
        safetyAlerts: [
          'Mantenha a porta aberta e apoiada por baixo ao reapertar parafusos da dobradiça.',
          'Não tente limar a chapa metálica do batente nem desbastar a madeira da porta sem experiência.',
          'Teste a chave e a maçaneta várias vezes com a porta aberta antes de fechá-la no batente.'
        ],
        hypothesis: 'Como a fechadura funciona suavemente com a porta aberta e só falha ao fechar, é possível que a folha da porta tenha cedido alguns milímetros por folga nos parafusos da dobradiça superior, fazendo a lingueta esbarrar na borda da chapa-testa.',
        whatToDo: 'Confira na Etapa 3 do nosso guia revisado como verificar e reapertar os parafusos da dobradiça superior com segurança.',
        guideSectionLabel: 'Ir para a Etapa 3: Corrigir pequeno desalinhamento nas dobradiças',
        guideUrl: 'artigos/como-consertar-fechadura-de-porta.html',
        whenToCallPro: 'Se os parafusos já estiverem firmes e a lingueta continuar fora de centro em relação ao batente, chame um marceneiro ou chaveiro para ajustar a chapa-testa.'
      },
      out_profissional_chave_ou_seguranca: {
        id: 'out_profissional_chave_ou_seguranca',
        actionType: 'profissional',
        badgeText: 'Recomendação: Chamar Profissional',
        title: 'Pare e acione um chaveiro profissional',
        safetyAlerts: [
          'Não tente girar chave trincada com alicate nem introduza pinças, colas ou arames para pescar pedaços de chave quebrada no cilindro.',
          'Se for a porta de entrada principal, não desmonte componentes que possam deixar o imóvel aberto ou trancar moradores do lado de fora.'
        ],
        hypothesis: 'Há hipótese de fratura da lâmina da chave dentro do cilindro ou falha crítica de travamento em porta de segurança residencial.',
        whatToDo: 'Este cenário envolve risco de inutilizar o cilindro ou comprometer o fechamento do imóvel e exige ferramentas próprias de extração ou substituição.',
        guideSectionLabel: 'Ver seção "Quando parar e chamar um profissional" no guia',
        guideUrl: 'artigos/como-consertar-fechadura-de-porta.html',
        whenToCallPro: 'Chame um chaveiro profissional imediatamente para extrair o fragmento ou substituir o cilindro com segurança.'
      },
      out_profissional_eletronica: {
        id: 'out_profissional_eletronica',
        actionType: 'profissional',
        badgeText: 'Fora do escopo para iniciantes • Assistência Técnica',
        title: 'Fechadura eletrônica/digital: consulte o manual ou assistência autorizada',
        safetyAlerts: [
          'NÃO aplique grafite em pó em fechaduras eletrônicas (o grafite conduz eletricidade e pode causar curto-circuito na placa).',
          'NÃO aplique sprays lubrificantes líquidos em sensores biométricos, teclados ou motores internos.'
        ],
        hypothesis: 'Em fechaduras digitais, falhas de acionamento costumam estar associadas a carga baixa das pilhas alcalinas, desalinhamento do batente ou falha no motor/circuito eletrônico.',
        whatToDo: 'O Conserte Agora possui guias apenas para fechaduras mecânicas tradicionais. Para modelos digitais, limite-se à troca de pilhas prevista no manual do fabricante ou acione a assistência técnica da marca.',
        guideSectionLabel: null,
        guideUrl: null,
        whenToCallPro: 'Se a troca de pilhas indicada no manual do fabricante não resolver, acione o suporte técnico autorizado da marca da fechadura.'
      },
      out_profissional_mecanismo_interno: {
        id: 'out_profissional_mecanismo_interno',
        actionType: 'profissional',
        badgeText: 'Exige desmontagem interna • Chamar Profissional',
        title: 'Hipótese de falha interna na máquina da fechadura: chame um chaveiro',
        safetyAlerts: [
          'NÃO retire a fechadura da madeira nem abra a tampa lateral da caixa metálica interna (as molas internas estão sob tensão e podem saltar ou travar o trinco definitivamente).',
          'Mantenha a porta aberta ou destrancada até a avaliação profissional para evitar que o trinco trave fechado.'
        ],
        hypothesis: 'Quando a maçaneta desce em falso sem puxar a lingueta ou a chave gira 360° sem acionar a tranca, a hipótese mais provável é o rompimento de mola interna, quebra da garrinha do trinco ou desgaste do came do cilindro.',
        whatToDo: 'Como esse reparo exige retirar a caixa da fechadura da porta e substituir peças internas, ele não deve ser feito por iniciantes.',
        guideSectionLabel: 'Consultar limites de segurança no guia de fechaduras',
        guideUrl: 'artigos/como-consertar-fechadura-de-porta.html',
        whenToCallPro: 'Acione um chaveiro profissional para substituir o mecanismo interno ou o cilindro compatível (padrão ABNT NBR 14913).'
      },
      out_profissional_marcenaria: {
        id: 'out_profissional_marcenaria',
        actionType: 'profissional',
        badgeText: 'Exige ajuste de marcenaria • Chamar Profissional',
        title: 'Hipótese de empenamento da madeira ou furos espanados: chame um marceneiro',
        safetyAlerts: [
          'Não force o fechamento da porta com pancadas (isso pode estourar as dobradiças ou rachar o batente).',
          'Não tente usar formão, plaina ou serra na folha da porta sem prática e bancada adequada.'
        ],
        hypothesis: 'Quando a madeira incha por umidade, raspa no piso ou os parafusos giram sem aperto na madeira esfarelada, o simples reaperto de chave de fenda não sustenta a folha da porta.',
        whatToDo: 'Esse caso exige restauração da furação na madeira, ajuste de marcenaria na folha/batente ou reposicionamento da chapa-testa.',
        guideSectionLabel: 'Ver seção "Como reconhecer que não resolveu" no guia',
        guideUrl: 'artigos/como-consertar-fechadura-de-porta.html',
        whenToCallPro: 'Chame um marceneiro ou carpinteiro para restaurar a fixação das dobradiças e alinhar a folha da porta.'
      },
      out_informacao_insuficiente: {
        id: 'out_informacao_insuficiente',
        actionType: 'informacao_insuficiente',
        badgeText: 'Informação insuficiente para indicar uma hipótese',
        title: 'Não há informação suficiente para sugerir um passo específico',
        safetyAlerts: [
          'Por precaução, não force a chave, não aplique óleos líquidos no cilindro e não desmonte a fechadura com a porta fechada.',
          'Se a porta correr qualquer risco de travar fechada com pessoas dentro do cômodo, mantenha-a aberta com um calço.'
        ],
        hypothesis: 'Com os sintomas informados até aqui, não é possível distinguir com segurança se o problema é falta de lubrificação, parafuso externo frouxo, desalinhamento da porta ou peça interna quebrada.',
        whatToDo: 'Recomendamos ler as verificações visuais básicas do nosso guia de fechaduras (sem desmontar nada) ou, na dúvida, solicitar a avaliação presencial de um chaveiro.',
        guideSectionLabel: 'Ler o guia completo de verificação básica de fechaduras',
        guideUrl: 'artigos/como-consertar-fechadura-de-porta.html',
        whenToCallPro: 'Se o sintoma envolver barulho de peça solta dentro da porta, chave prendendo ao sair ou porta de entrada principal, chame diretamente um chaveiro.'
      }
    }
  };

  function getFlowDefinition() {
    return FLOW;
  }

  function getQuestion(questionId) {
    const id = questionId || 'q1_triagem';
    return FLOW.questions[id] || null;
  }

  function evaluateAnswer(questionId, optionId) {
    const q = getQuestion(questionId);
    if (!q) return { error: 'Pergunta inválida' };
    const opt = q.options.find(o => o.id === optionId);
    if (!opt) return { error: 'Opção inválida' };

    if (opt.nextQuestion) {
      return {
        type: 'question',
        question: getQuestion(opt.nextQuestion),
        selectedOption: opt
      };
    }
    if (opt.outcome && FLOW.outcomes[opt.outcome]) {
      return {
        type: 'outcome',
        outcome: FLOW.outcomes[opt.outcome],
        selectedOption: opt
      };
    }
    return {
      type: 'outcome',
      outcome: FLOW.outcomes.out_informacao_insuficiente,
      selectedOption: opt
    };
  }

  return {
    getFlowDefinition,
    getQuestion,
    evaluateAnswer
  };
});
