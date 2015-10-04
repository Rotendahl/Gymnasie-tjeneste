(TeX-add-style-hook
 "lol"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "inputenc"
    "fontenc"
    "stmaryrd"
    "fancyhdr"
    "natbib"
    "graphicx"
    "amsmath"
    "amssymb"
    "pgf"
    "tikz"
    "listings"
    "color")
   (TeX-add-symbols
    "Fin")
   (LaTeX-add-labels
    "FIN")))

