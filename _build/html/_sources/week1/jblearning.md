# Day 1 learning about JupyterCon Tutorial 2020 (18 Jan 2022)

## File type in jupyter notebook

There are many filetypes in jupyter book, we can use it to develop file to compile a page to see. Which includes:
1. .md : Markdown file
2. .ipynb : jupyter notebook file

---

## Process from source file to rendered file

We cannot read the file directly from the .md file, so we will need to render it into human-readable pages in order to make it readable.

The source file(.md, .ipynb, .myst) will converted in to jupyter notebook for the machine to execute and cacheing those output in code-cell for the purpose of show to audiance. Then it will render into different files such as .pdf, .html, and so on.

---

## additional content for a better reading experience in jupyter book

there are a lot of extra style in jupyter book in different looking for senmantic content block
1. Admonition block
	```{admonition} This is a admonition block
	We can put text inside here to make admonition
	```
	We can also add style into admonition block such as tips.
2. Admonition block with tip class
	```{admonition} This is a admonition tip block
	:class: tip
	We can put text inside here to make admonition
	```
3. Figures and captions
	We can add figures into the page to enhance your point:
	```{figure} /rick.jpg
	This is a picture to rick roll you
	```
4. Drop down block
	We can add a class called 'dropdown' to hide the block

	```{admonition} Rick Roll
	:class: dropdown
	Never gonna let you down
	```

---

## Thing that I noticed

I found that you have to remove the whole _build file to make your page update completly, or it will remain some old data or cache inside the page and cause the navigation bugged.
+++
Also, the compiler will automatically update the figure number for you to save you some time from re-entering the figure number whenn you inserted or deleted some figure.