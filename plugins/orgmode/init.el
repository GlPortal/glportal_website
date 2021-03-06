;; Init file to use with the orgmode plugin.

;; Load org-mode
;; Requires org-mode v8.x

;; Uncomment these lines and change the path to your org source to
;; add use it.
;; (let* ((org-lisp-dir "~/.emacs.d/src/org/lisp"))
;;   (when (file-directory-p org-lisp-dir)
;;       (add-to-list 'load-path org-lisp-dir)
;;       (require 'org)))

(require 'ox-html)

;;; Custom configuration for the export. ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;; Add any custom configuration that you would like to 'conf.el'.
(setq
 org-export-with-toc nil
 org-export-with-section-numbers nil
 org-startup-folded 'showeverything)

;; Load additional configuration from conf.el
(let ((conf (expand-file-name "conf.el" (file-name-directory load-file-name))))
  (if (file-exists-p conf)
      (load-file conf)))

;;; Macros ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Load Nikola macros
(setq nikola-macro-templates
      (with-current-buffer
          (find-file
           (expand-file-name "macros.org" (file-name-directory load-file-name)))
        (org-macro--collect-macros)))


;;; Code highlighting ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Use pygments highlighting for code
(defun pygmentize (lang code)
  "Use Pygments to highlight the given code and return the output"
  (with-temp-buffer
    (insert code)
    (let ((lang (or (cdr (assoc lang org-pygments-language-alist)) "text")))
      (shell-command-on-region (point-min) (point-max)
                               (format "pygmentize -f html -g -l %s" lang)
                               (buffer-name) t))

    (buffer-string)))


(defconst org-pygments-language-alist
  '(
    ("asymptote" . "asymptote")
    ("awk" . "awk")
    ("C" . "c")
    ("cpp" . "cpp")
    ("clojure" . "clojure")
    ("css" . "css")
    ("D" . "d")
    ("emacs-lisp" . "scheme")
    ("F90" . "fortran")
    ("gnuplot" . "gnuplot")
    ("groovy" . "groovy")
    ("haskell" . "haskell")
    ("java" . "java")
    ("js" . "js")
    ("julia" . "julia")
    ("latex" . "latex")
    ("lisp" . "lisp")
    ("makefile" . "makefile")
    ("matlab" . "matlab")
    ("mscgen" . "mscgen")
    ("ocaml" . "ocaml")
    ("octave" . "octave")
    ("perl" . "perl")
    ("picolisp" . "scheme")
    ("python" . "python")
    ("R" . "r")
    ("ruby" . "ruby")
    ("sass" . "sass")
    ("scala" . "scala")
    ("scheme" . "scheme")
    ("sh" . "sh")
    ("sql" . "sql")
    ("sqlite" . "sqlite3")
    ("tcl" . "tcl")
    )
  "Alist between org-babel languages and Pygments lexers.

See: http://orgmode.org/worg/org-contrib/babel/languages.html and
http://pygments.org/docs/lexers/ for adding new languages to the
mapping. ")

;; Override the html export function to use pygments
(defun org-html-src-block (src-block contents info)
  "Transcode a SRC-BLOCK element from Org to HTML.
CONTENTS holds the contents of the item.  INFO is a plist holding
contextual information."
  (if (org-export-read-attribute :attr_html src-block :textarea)
      (org-html--textarea-block src-block)
    (let ((lang (org-element-property :language src-block))
	  (code (org-html-format-code src-block info)))
      (if (and (org-export-read-attribute :attr_html src-block :bootstrap)
               (string-equal lang 'org))
          (bootstrapize src-block)
        (pygmentize lang code)))))


(defun bootstrapize (src-block)
  (let (
        (text (car (org-export-unravel-code src-block)))
        (component (org-export-read-attribute :attr_html src-block :component))
        (title (org-export-read-attribute :attr_html src-block :title))
        (extra-class (org-export-read-attribute :attr_html src-block :extra-class))
        html)

    (with-temp-buffer
      (insert text)
      (org-macro-replace-all nikola-macro-templates)
      (org-html-export-as-html nil nil t t)
      (setq html (buffer-string))
      (kill-buffer))
    (cond((equal component "panel")
          (format "<div class=\"panel panel-default %s\">\n  <div class=\"panel-body\">\n %s \n  </div>\n</div>\n" (or extra-class "") html))
         ((equal component "main-panel")
          (format "<div class=\"%s\"><div class=\"panel panel-primary\">\n  <div class=\"panel-heading\"><h2>%s</h2></div><div class=\"panel-body\">\n %s \n  </div>\n</div>\n</div>\n</div>\n" (or extra-class "") title html))
         ((equal component "default-panel")
          (format "<div class=\"%s\"><div class=\"panel panel-default\">\n  <div class=\"panel-heading\"><h2>%s</h2></div><div class=\"panel-body\">\n %s \n  </div>\n</div>\n</div>\n</div>\n" (or extra-class "") title html))
         ((equal component nil)
          (format "<div class=\"%s\">\n %s \n </div>\n" (or extra-class "") html))
          (t
           (format "<div class=\"%s %s\">\n %s </div>\n" component (or extra-class "") html)))
          )
         )


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Export function used by Nikola.
(defun nikola-html-export (infile outfile)
  "Export the body only of the input file and write it to
specified location."

  (with-current-buffer (find-file infile)
    (org-macro-replace-all nikola-macro-templates)
    (org-html-export-as-html nil nil t t)
    (write-file outfile nil)))
