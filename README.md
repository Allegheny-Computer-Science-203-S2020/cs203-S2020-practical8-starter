# cs203-S2020-practical8-starter

## Table of Contents

* [Introduction](#introduction)
* [Learning](#learning)
* [System Commands](#system-commands)
  + [Using Docker](#using-docker)
  + [Using Gradle](#using-gradle)
* [Using Pyenv and Pipenv](#using-pyenv-and-pipenv)
* [Expected Output](#expected-output)
* [Automated Checks with GatorGrader](#automated-checks-with-gatorgrader)
* [Updates](#updates)
* [Travis](#travis)
* [System Requirements](#system-requirements)
* [Reporting Problems](#reporting-problems)
* [Receiving Assistance](#receiving-assistance)
* [Project Assessment](#project-assessment)
* [Project Feedback](#project-feedback)

## Introduction

Designed for use with [GitHub Classroom](https://classroom.github.com/) and
[GatorGrader](https://github.com/GatorEducator/gatorgrader/), this repository
contains the starter for a laboratory assignment in a software engineering
course class that uses the Python programming language. The Travis CI builds for
this repository will pass, as evidenced by a green &#x2714; instead of a red
&#x2717; appearing in the commit logs. An instructor would use this repository
to create a "starter" repository with purposefully omitted features that a
student would then need to add in order to achieve the stated learning
objectives. Please bear in mind that much of the content in this document is
written in its current form under the assumption that it will also accompany the
"starter" repository that an instructor shares with a student through the use of
[GitHub Classroom](https://classroom.github.com/).

This assignment requires a programmer to refactor, document, and automatically
test a Python program called `termfrequency/compute_tf_aspects.py`.
Please refer to the Preface and Chapters 1 through 10 in "Exercises in
Programming Style" to learn more about this program's input, output, and
behavior. You can also review all of the chapters in "Think Python" to learn
more about how to program in Python and run Python scripts. You also will refer
to the first two chapters in the "Pytest" book. In addition to the work that you
did for the previous practical assignment &mdash; exploring different
command-line options for Pytest, installing the `pytest-cov` code coverage
calculation package, perform code coverage analysis, and incrementally
increasing the coverage of your test suite &mdash; you will gain experience with
refactoring Python source code so that it meets well-established standards for
source code formatting. Finally, the key task for this assignment is to learn
more about how the Python programming language supports the aspect-oriented
programming paradigm, as explain in Chapter 10 of the "Exercises in Programming
Style" book.

When you use the `git commit` command to transfer your source code to your
GitHub repository, [Travis CI](https://travis-ci.com/) will initialize a build
of your assignment, checking to see if it meets all of the requirements. If both
your source code and writing meet all of the established requirements, then you
will see a green &#x2714; in the listing of commits in GitHub. If your
submission does not meet the requirements, a red &#x2717; will appear instead.
The instructor will reduce a programmer's grade for this assignment if the red
&#x2717; appears on the last commit in GitHub immediately before the
assignment's due date.

## Learning

If you have not done so already, please read all of the relevant [GitHub
Guides](https://guides.github.com/) that explain how to use many of the features
that GitHub provides. In particular, please make sure that you have read the
following GitHub guides: [Mastering
Markdown](https://guides.github.com/features/mastering-markdown/), [Hello
World](https://guides.github.com/activities/hello-world/), and [Documenting Your
Projects on GitHub](https://guides.github.com/features/wikis/). Each of these
guides will help you to understand how to use both [GitHub](http://github.com) and
[GitHub Classroom](https://classroom.github.com/).

To do well on this assignment, you should also read Chapters 1 and 2 in "Think
Python", paying particularly close attention to the content about variables,
expressions, and statements. You should also read the Preface and Chapters 1
through 10 in the "Exercises in Programming Style" book. Finally, you should read
online articles about coverage testing with Pytest and
[Coverage.py](https://github.com/nedbat/coveragepy). Please see the course
instructor or one of the teaching assistants or tutors if you have questions
about any of these reading assignments.

## System Commands

This project invites students to enter system commands into a terminal window.
This assignment uses [Docker](https://www.docker.com) to deliver programs, such
as `gradle` and the source code and packages needed to run
[GatorGrader](https://github.com/GatorEducator/gatorgrader), to a students'
computer, thereby eliminating the need for a programmer to install them on their
development workstation. Along with using Docker for automated grading and
assessment on your laptop, students are also asked to setup a full-fledged
Python development environment that leverages
[Pyenv](https://github.com/pyenv/pyenv) to download and manage versions of
Python and [Pipenv](https://github.com/pypa/pipenv) to install and manage Python
packages.

### Using Docker

Once you have installed [Docker
Desktop](https://www.docker.com/products/docker-desktop), with MacOS and Linux
you can use the following `docker run` command to start `gradle grade` as a
containerized application, using the
[DockaGator](https://github.com/GatorEducator/dockagator) Docker image available
on
[DockerHub](https://cloud.docker.com/u/gatoreducator/repository/docker/gatoreducator/dockagator).

```bash
docker run --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator
```

The aforementioned command will use `"$(pwd)"` (i.e., the current working
directory) as the project directory and `"$HOME/.dockagator"` as the cached
GatorGrader directory. Please note that both of these directories must exist,
although only the project directory must contain something. Generally, the
project directory should contain the source code and technical writing for this
assignment, as provided to a student by the instructor through GitHub.
Additionally, the cache directory should not contain anything other than
directories and programs created by DockaGator, thus ensuring that they are not
otherwise overwritten during the completion of the assignment. To ensure that
the previous command will work correctly, you should create the cache directory
by running the command `mkdir $HOME/.dockagator` on the MacOS and Linux
operating systems. However, if you are using the Windows operating system then
you will instead need to type the command `mkdir
%HomeDrive%%HomePath%/.dockagator`. Finally, if the above `docker run` command
does not work correctly on the Windows operating system, you may need to instead
run the following command to adapt to the differences in the `cmd` terminal
window:

```bash
docker run --rm --name dockagator \
  -v "%cd%:/project" \
  -v "%HomeDrive%%HomePath%/.dockagator:/root/.local/share" \
  gatoreducator/dockagator
```

Here are some additional commands that you may need to run when using Docker:

* `docker info`: display information about how Docker runs on your workstation
* `docker images`: show the Docker images installed on your workstation
* `docker container list`: list the active images running on your workstation
* `docker system prune`: remove many types of "dangling" components from your workstation
* `docker image prune`: remove all "dangling" docker images from your workstation
* `docker container prune`: remove all stopped docker containers from your workstation
* `docker rmi $(docker images -q) --force`: remove all docker images from your workstation

### Using Gradle

Since the above `docker run` command uses a Docker images that, by default, runs
`gradle grade` and then exits the Docker container, you may want to instead run
the following command so that you enter an "interactive terminal" that will
allow you to repeatedly run commands within the Docker container. Don't forget
that, if you are using the Windows operating system, then you will need to use a
different command to run Docker, as explained previously in this document.

```bash
docker run -it --rm --name dockagator \
  -v "$(pwd)":/project \
  -v "$HOME/.dockagator":/root/.local/share \
  gatoreducator/dockagator /bin/bash
```

Once you have typed this command, you can use the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader) in the Docker container by
typing the command `gradle grade` in your terminal. Running this command will
produce a lot of output that you should carefully inspect. If GatorGrader's
output shows that there are no mistakes in the assignment, then your source code
and writing are passing all of the automated baseline checks. However, if the
output indicates that there are mistakes, then you will need to understand what
they are and then try to fix them.

You can also complete several important Python programming tasks by using the
`gradle` tool. For instance, you can compile (i.e., create bytecode from the
program's source code if it is correct) the program using the command `gradle
build`. Here are some other commands that you can type:

* `gradle grade`: run the [GatorGrader](https://github.com/GatorEducator/gatorgrader) tool to check your work
* `gradle tasks`: display details about the Gradle system

To run one of these commands, you must be in the main (i.e., "home base")
directory for this assignment where the `build.gradle` file is located.

## Using Pyenv and Pipenv

Assuming that you will use [Pyenv](https://github.com/pyenv/pyenv) to download
and manage your installation of Python, this practical assignment also invites
you to use [Pipenv](https://github.com/pypa/pipenv) to create a virtual
environment, install and manage development packages, and to run Python
commands. Here is a sample of the Pipenv commands that you will need to run
during this assignment.

- Install and upgrade the `pipenv` command: `pip install pipenv --user`
- Install the development dependencies: `pipenv` command: `pipenv install --dev`
- Run the linters and the formatter to check your Python source code: `pipenv run lint --check`
- Run the test suite to check your Python source code: `pipenv run test`
- Run the test suite and calculate test suite coverage: `pipenv run cover`
- Run the program with `pipenv` and `python` and a small input: `pipenv run python termfrequency/compute_tf_aspects.py inputs/input.txt`
- Run the program with `pipenv` and `python` and a realistic input: `pipenv run python termfrequency/compute_tf_aspects.py inputs/pride-and-prejudice.txt`

To run one of these commands, you must be in the main directory for this
assignment where the configuration files are located. Then, you can type these
commands in the terminal and study the output.

## Expected Output

Running the program with the small input should produce the following output:

```
extract_words(...) took 0.00026106834411621094 secs
frequencies(...) took 4.76837158203125e-06 secs
sort(...) took 7.62939453125e-06 secs
live  -  2
mostly  -  2
white  -  1
tigers  -  1
india  -  1
wild  -  1
lions  -  1
africa  -  1
```

Running the program with the realistic input should produce the following output:

```
extract_words(...) took 0.25045108795166016 secs
frequencies(...) took 0.011602401733398438 secs
sort(...) took 0.001898050308227539 secs
mr  -  786
elizabeth  -  635
very  -  488
darcy  -  418
such  -  395
mrs  -  343
much  -  329
more  -  327
bennet  -  323
bingley  -  306
jane  -  295
miss  -  283
one  -  275
know  -  239
before  -  229
herself  -  227
though  -  226
well  -  224
never  -  220
sister  -  218
soon  -  216
think  -  211
now  -  209
time  -  203
good  -  201
```

## Automated Checks with GatorGrader

In addition to meeting all of the requirements outlined in the assignment sheet,
your submission must pass the following checks that
[GatorGrader](https://github.com/GatorEducator/gatorgrader) automatically
assesses:

- The compute_tf_aspects.py in termfrequency has at least 3 single-line Python comment(s)
- The compute_tf_aspects.py in termfrequency has at least 6 multiple-line Python comment(s)
- The compute_tf_aspects.py in termfrequency has exactly 0 of the `TODO` fragment
- The conftest.py in tests has exactly 0 of the `TODO` fragment
- The cover.sh in scripts has exactly 0 of the `TODO` fragment
- The file compute_tf_aspects.py exists in the termfrequency directory
- The file conftest.py exists in the tests directory
- The file cover.sh exists in the scripts directory
- The file __init__.py exists in the tests directory
- The file lint.sh exists in the scripts directory
- The file reflection.md exists in the writing directory
- The file test_compute_tf_aspects.py exists in the tests directory
- The file test.sh exists in the scripts directory
- The __init__.py in tests has exactly 0 of the `TODO` fragment
- The lint.sh in scripts has exactly 0 of the `TODO` fragment
- The reflection.md in writing has at least 500 word(s) in total
- The reflection.md in writing has exactly 0 of the `Add Your Name Here` fragment
- The reflection.md in writing has exactly 0 of the `TODO` fragment
- The reflection.md in writing has exactly 6 of the `heading` tag
- The repository has at least 5 commit(s)
- The test_compute_tf_aspects.py in tests has at least 0 single-line Python comment(s)
- The test_compute_tf_aspects.py in tests has at least 2 of the `assert` fragment
- The test_compute_tf_aspects.py in tests has at least 2 of the `test_` fragment
- The test_compute_tf_aspects.py in tests has at least 3 multiple-line Python comment(s)
- The test_compute_tf_aspects.py in tests has exactly 0 of the `TODO` fragment
- The test.sh in scripts has exactly 0 of the `TODO` fragment

If [GatorGrader's](https://github.com/GatorEducator/gatorgrader) automated
checks pass correctly, the tool will produce the output like the following in
addition to returning a zero exit code (which you can access by typing the
command `echo $?`).

```
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Passed 26/26 (100%) of checks for cmpsc-203-spring-2020-practical8! ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Updates

If the course instructor updates the provided material for this assignment and
you would like to receive these updates, then you can type this command in the
main directory for this assignment:

```
git remote add download git@github.com:Allegheny-Computer-Science-203-S2020/cs203-S2020-practical8-starter.git
```

You should only need to type this command once; typing the command additional
times may yield an error message but will not negatively influence the state of
your repository. Now, you are ready to download the updates provided by the
course instructor by typing:

```
git pull download master
```

This second command can be run whenever the course instructor needs to provide
you with new source code for this assignment. However, please note that, if you
have edited the files that the course instructor updated, running the previous
command may lead to Git merge conflicts. If this happens, you may need to
manually resolve them with the help of the instructor or a teaching assistant.

## Travis

This assignment uses [Travis CI](https://travis-ci.com/) to automatically run
the checking programs every time you commit to your GitHub repository. The
checking will start as soon as you have accepted the assignment, thus creating
your own private repository, and the course instructor enables Travis for it. If
you are using Travis for the first time, you will need to authorize Travis CI to
access the private repositories that you created on GitHub.

## System Requirements

We developed this assignment to work with the following software and versions:

- Docker Desktop
- Operating Systems
  - Linux
  - MacOS
  - Windows 10 Pro
  - Windows 10 Enterprise
- Programming Language Tools
  - Gradle 5.4
  - MDL 0.5.0
  - OpenJDK 11.0.4
  - Proselint 0.10.2
  - Python 3.6 or 3.7

## Reporting Problems

If you have found a problem with this assignment's provided source code, then
you can go to the [Computer Science 203 Practical 8
Starter](https://github.com/Allegheny-Computer-Science-203-S2020/cs203-S2020-practical8-starter)
repository and create an issue by clicking the "Issues" tab and then clicking
the green "New Issue" button. If you have found a problem with the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader) and the way that it checks
you assignment, then you can follow the aforementioned steps to create an issue
in its repository. To ensure that your issue is properly resolved, please
provide as many details as is possible about the problem that you experienced.
If you discover a problem with the laboratory assignment sheet, then please
raise an issue in the
[cs203-S2020-sheets](https://github.com/Allegheny-Computer-Science-203-S2020/cs203-S2020-sheets)
repository and mention this assignment.

Students who find &mdash; and use the appropriate GitHub issue tracker to
correctly document &mdash; a mistake in any aspect of this laboratory assignment
will receive free GitHub stickers and extra credit towards their grade for it.

## Receiving Assistance

If you are having trouble completing any part of this project, then please talk
with either the course instructor or a student technical during the practical
session. Alternatively, you may ask questions in the Slack workspace for this
course. Finally, you can schedule a meeting during the course instructor's
office hours.

## Project Assessment

Taking inspiration from the principles of [specification-based
grading](http://rtalbert.org/return-to-specs-grading-calculus/), the grade that
a student receives on this assignment will have the following components:

- **Percentage of Correct GatorGrader Checks**: Students are encouraged to
  repeatedly try to implement a Java program that passes all of GatorGrader's
  checks by, for instance, creating a program that produces the correct output.
  Students should also repeatedly revise their technical writing to ensure that
  it also passes all of GatorGrader's checks about, for instance, the length of
  its content and its appropriate use of Markdown.

- **Travis CI Build Status**: Since additional checks on the source code and/or
  technical writing may be encoded in Travis CI's actions and, moreover, all of
  the GatorGrader checks are also run in Travis CI, students will receive a
  checkmark grade if their last before-the-deadline build passes and a green
  &#x2714; appears in their GitHub commit log instead of a red &#x2717;. As with
  the previous grading component, students are encouraged to repeatedly revise
  their source code and technical writing in an attempt to get their Travis CI
  build to pass.

- **Mastery of Technical Writing**: Students will also receive a checkmark grade
  when the responses to the technical writing questions presented in the
  `writing/reflection.md` reveal a mastery of both writing skills and technical
  knowledge. To receive a checkmark grade, the submitted writing should have
  correct spelling, grammar, and punctuation in addition to following the rules
  of Markdown and providing technically accurate answers. Students are
  encouraged to ask the course instructor or a student technical leader to use
  the GitHub issue tracker to provide feedback on their mastery of technical
  writing skills.

- **Mastery of Technical Knowledge and Skills**: Students will receive also
  receive a checkmark grade when their GitHub repository reveals that they have
  mastered all the technical knowledge and skills developed during the
  completion of this project. As a part of this grade, the instructor will
  assess aspects of the project including, but not limited to, the inclusion of
  effective source code comments, creation of Git commit messages, correct use
  of Docker, and correct installation and use of a full-fledge Python
  development environment. Students are encouraged to ask the course instructor
  or a student technical leader to use the GitHub issue tracker to provide
  feedback on how well their work demonstrates mastery of the assignment's
  technical knowledge and skills.

All grades for this project will be reported through a student's GitHub
repository using either messages in the GitHub commit log or issues raised in
the issue tracker. Students should ask questions about their grade for this
project in GitHub so as to facilitate an effective conversation about the
submitted deliverables.

## Project Feedback

Students who wish to receive feedback on their work for this practical
assignment should first open an issue on the issue tracker for this GitHub
repository, giving an appropriate title and description for the type of feedback
that you would like the course instructor to provide. After creating this issue,
you will see that GitHub has created a unique web site that references this
issue. To alert the course instructor to the fact that the issue was created and
that you want feedback on your work, please send it to him by a Slack direct
message at least 24 hours in advance of the project's due date. After the
instructor responds to the issue, please resolve all of the stated concerns and
participate in the discussion until the issue is closed.
