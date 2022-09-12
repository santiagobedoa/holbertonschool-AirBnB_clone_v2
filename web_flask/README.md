# 0x04. AirBnB clone - Web framework

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <h2>
   Resources
  </h2>
  <p>
   <strong>
    Read or watch
   </strong>
   :
  </p>
  <ul>
   <li>
    <a href="https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb" target="_blank" title="What is a Web Framework?">
     What is a Web Framework?
    </a>
   </li>
   <li>
    <a href="https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application" target="_blank" title="A Minimal Application">
     A Minimal Application
    </a>
   </li>
   <li>
    <a href="https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing" target="_blank" title="Routing">
     Routing
    </a>
    (
    <em>
     except “HTTP Methods”
    </em>
    )
   </li>
   <li>
    <a href="https://flask.palletsprojects.com/en/2.0.x/quickstart/#rendering-templates" target="_blank" title="Rendering Templates">
     Rendering Templates
    </a>
   </li>
   <li>
    <a href="https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis" target="_blank" title="Synopsis">
     Synopsis
    </a>
   </li>
   <li>
    <a href="https://jinja.palletsprojects.com/en/2.9.x/templates/#variables" target="_blank" title="Variables">
     Variables
    </a>
   </li>
   <li>
    <a href="https://jinja.palletsprojects.com/en/2.9.x/templates/#comments" target="_blank" title="Comments">
     Comments
    </a>
   </li>
   <li>
    <a href="https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control" target="_blank" title="Whitespace Control">
     Whitespace Control
    </a>
   </li>
   <li>
    <a href="https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures" target="_blank" title="List of Control Structures">
     List of Control Structures
    </a>
    (
    <em>
     read up to “Call”
    </em>
    )
   </li>
   <li>
    <a href="https://palletsprojects.com/p/flask/" target="_blank" title="Flask">
     Flask
    </a>
   </li>
   <li>
    <a href="https://jinja.palletsprojects.com/en/2.9.x/templates/" target="_blank" title="Jinja">
     Jinja
    </a>
   </li>
  </ul>
  <h2>
   Learning Objectives
  </h2>
  <p>
   At the end of this project, you are expected to be able to
   <a href="https://fs.blog/feynman-learning-technique/" target="_blank" title="explain to anyone">
    explain to anyone
   </a>
   ,
   <strong>
    without the help of Google
   </strong>
   :
  </p>
  <h3>
   General
  </h3>
  <ul>
   <li>
    What is a Web Framework
   </li>
   <li>
    How to build a web framework with Flask
   </li>
   <li>
    How to define routes in Flask
   </li>
   <li>
    What is a route
   </li>
   <li>
    How to handle variables in a route
   </li>
   <li>
    What is a template
   </li>
   <li>
    How to create a HTML response in Flask by using a template
   </li>
   <li>
    How to create a dynamic template (loops, conditions…)
   </li>
   <li>
    How to display in HTML data from a MySQL database
   </li>
  </ul>
  <h2>
   Requirements
  </h2>
  <h3>
   Python Scripts
  </h3>
  <ul>
   <li>
    Allowed editors:
    <code>
     vi
    </code>
    ,
    <code>
     vim
    </code>
    ,
    <code>
     emacs
    </code>
   </li>
   <li>
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using
    <code>
     python3
    </code>
    (version 3.4.3)
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    The first line of all your files should be exactly
    <code>
     #!/usr/bin/python3
    </code>
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, is mandatory
   </li>
   <li>
    Your code should use the
    <code>
     PEP 8
    </code>
    style (version 1.7)
   </li>
   <li>
    All your files must be executable
   </li>
   <li>
    The length of your files will be tested using
    <code>
     wc
    </code>
   </li>
   <li>
    All your modules should have documentation (
    <code>
     python3 -c 'print(__import__("my_module").__doc__)'
    </code>
    )
   </li>
   <li>
    All your classes should have documentation (
    <code>
     python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    </code>
    )
   </li>
   <li>
    All your functions (inside and outside a class) should have documentation (
    <code>
     python3 -c 'print(__import__("my_module").my_function.__doc__)'
    </code>
    and
    <code>
     python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    </code>
    )
   </li>
   <li>
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
   </li>
  </ul>
  <h3>
   HTML/CSS Files
  </h3>
  <ul>
   <li>
    Allowed editors:
    <code>
     vi
    </code>
    ,
    <code>
     vim
    </code>
    ,
    <code>
     emacs
    </code>
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file at the root of the folder of the project is mandatory
   </li>
   <li>
    Your code should be W3C compliant and validate with
    <a href="https://github.com/holbertonschool/W3C-Validator" target="_blank" title="W3C-Validator">
     W3C-Validator
    </a>
    (except for jinja template)
   </li>
   <li>
    All your CSS files should be in the
    <code>
     styles
    </code>
    folder
   </li>
   <li>
    All your images should be in the
    <code>
     images
    </code>
    folder
   </li>
   <li>
    You are not allowed to use
    <code>
     !important
    </code>
    or
    <code>
     id
    </code>
    (
    <code>
     #...
    </code>
    in the CSS file)
   </li>
   <li>
    Current screenshots have been done on
    <code>
     Chrome 56.0.2924.87
    </code>
    .
   </li>
   <li>
    No cross browsers
   </li>
  </ul>
  <h2>
   More Info
  </h2>
  <h3>
   Install Flask
  </h3>
  <pre><code>$ pip3 install Flask
</code></pre>
  <p>
   <img alt="" loading="lazy" src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png" style=""/>
  </p>
  <iframe allowfullscreen="" frameborder="0" height="315" src="https://www.youtube.com/embed/lzs4nQOiZQY" width="560">
  </iframe>
  <h3>
   Manual QA Review
  </h3>
  <p>
   <strong>
    It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.
   </strong>
  </p>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/290)
</html>