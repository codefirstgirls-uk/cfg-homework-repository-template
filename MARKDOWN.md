# Markdown Guide

Hello and welcome to a brief markdown guide!

Markdown files are simple text files which some minor syntax to allow content to be structured effectively. They are rendered, transforming the syntax into the visual equivilent (similar to html!).

The nice thing about markdown files is that they can be written on any os, on any editor, AND they are both commentable and render in GitHub. They are used **EVERYWHERE** in industry and you'll need to be able to write one to document and describe your software to collaborate with others.

# .md files

You can creata a new markdown file by creating a new file in your editor and specifying the .md extension, say homework1.md. If you try to open this file in pycharm, you should see a second tab open up in your editor in which the file will be rendered. This makes the ## expand the text etc.

If you are using vscode, see this guide on how to setup markdown rendering: https://code.visualstudio.com/docs/languages/markdown.

## Syntax Examples

Here's are some of the most common syntax that
you might use (don't worry! It's not as plentiful as Python or SQL!)

### Headers

# Header
## Smaller header
### Smaller header
#### Smaller header
##### Smallest header

A list can be defined in a dot format or by number order:

1. Item One
2. Item Two
3. Item Three

- Some item
- Another item
- And then some!

### What about tables?

You can do that too! See the below syntax:

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

### What about images and code?

It is possible to inject both code AND images if you need too. Generally though, you will be fine with submitting python files (.py) and a markdown file (.md) for the text based questions.
Image

If you find the need for an image, you can create an image directory in the same directory as your markdown file and use the following syntax:

![A cat](./images/cat.jpeg "Cat")

If you want to code instead you just need to indent the code:

    worlds = [1,2,3]
    for world in worlds:
        print(f"hello world #{world}!")

Note that you should **always** favour writing code in actual code files (e.g. .sql or .py), especially when providing answers to homeworks.

## Homework X Sample Submission

### Questions

1. Question goes here? If there a multiple sections (say both SQL and Python theory),
you can split these into 

Answer goes here. Can be a chunk of text, paragraphs or a list:

2. Can you indent a list?
- Yes
   - You totally
        - Can!