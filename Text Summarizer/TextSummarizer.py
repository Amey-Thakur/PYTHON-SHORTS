from gensim.summarization import summarize

text = "In late summer 1945, guests are gathered for the wedding reception of Don Vito Corleones " + \
       "daughter Connie (Talia Shire) and Carlo Rizzi (Gianni Russo). Vito (Marlon Brando),"  + \
       "the head of the Corleone Mafia family, is known to friends and associates as Godfather. "  + \
       "He and Tom Hagen (Robert Duvall), the Corleone family lawyer, are hearing requests for favors "  + \
       "because, according to Italian tradition, no Sicilian can refuse a request on his daughter's wedding " + \
       " day. One of the men who asks the Don for a favor is Amerigo Bonasera, a successful mortician "  + \
       "and acquaintance of the Don, whose daughter was brutally beaten by two young men because she"  + \
       "refused their advances; the men received minimal punishment from the presiding judge. " + \
       "The Don is disappointed in Bonasera, who'd avoided most contact with the Don due to Corleone's" + \
       "nefarious business dealings. The Don's wife is godmother to Bonasera's shamed daughter, " + \
       "a relationship the Don uses to extract new loyalty from the undertaker. The Don agrees " + \
       "to have his men punish the young men responsible (in a non-lethal manner) in return for " + \
        "future service if necessary."
          
print (summarize(text))
