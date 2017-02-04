#!/usr/bin/env python3
import os
from pweave import Pweb, PwebTexPweaveFormatter

filenames = [
    "expdistribution",
    "constructiondiscretetime",
    "constructioncontinuoustime",
    "ratestability",
    "empericalperfmeasures",
    "levelcrossing",
    "ratestability",
    "mm1",
    "mnmn1",
    "pasta",
    "little",
    "usefulidentities",
    "mg1",
    "batcharrivals",
    "mg1distributionqueuelength",
    "mg1density",
    "gg1",
    "serviceInterruptions",
    "process_batches",
    "tandem",
    "convolution",
    "mva",
    "mda",
]

filenames = [
    "mda",
      ]

to_dir = r"chunks/"

if not os.path.exists(to_dir):
    os.makedirs(to_dir)

class ToFile(PwebTexPweaveFormatter):
    chunks = []

    def preformat_chunk(self, chunk):
        ToFile.chunks.append(chunk.copy())  # Store the chunks
        if chunk['type'] == 'code':
            source = os.path.splitext(self.source)[0]
            fname = "chunks/{}_{}.tex".format(source, chunk['number'])
            with open(fname, "w") as f:
                if chunk['term']:
                    f.write(chunk['result'])
                    chunk['result'] = r"\lstinputlisting{"+fname+"}"
                else:
                    f.write(chunk['content'])
                    f.write(chunk['result'])
                    chunk['content'] = r"\lstinputlisting{"+fname+"}"
                    chunk['result'] = "\n\n"
        return(chunk)


for fname in filenames:
    doc = Pweb(fname+r".tex", format="texpweave", output=to_dir+fname+r".tx")
    doc.setformat(Formatter=ToFile)
    doc.updateformat({
        "outputstart": "\n",
        "outputend": "\n",
        "codestart": "\n",
        "codeend": "\n",
        "termstart": "\n",
        "termend": "\n",
    }
    )
#     doc.updateformat({
#         "outputstart": r"\begin{lstlisting}",
#         "outputend": r"\end{lstlisting}",
#         "codestart": r"\begin{lstlisting}",
#         "codeend": r"\end{lstlisting}",
#         "termstart": r"\begin{lstlisting}",
#         "termend": r"\end{lstlisting}",
#     }
#     )
    doc.weave()
