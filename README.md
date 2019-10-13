# hello
helloworld project for test

# what's a sharp punctuation?
	online edit
	edited at host1

# The <i>ADD</i> command is confusing for a SVN user.

Here is [a brief tutorial](https://www.atlassian.com/git/tutorials/using-branches/git-merge).

- # Start a new feature

~~~
git checkout -b new-feature master
~~~

- # Edit some files

~~~
git add <file>
git commit -m "Start a feature"
~~~

- # Edit some files

~~~
git add <file>
git commit -m "Finish a feature"
~~~

- # Merge in the new-feature branch

~~~
git checkout master
git merge new-feature
git branch -d new-feature
~~~

## Manage Branch

- list branch, create branch, swith branch

~~~
    git branch
    git branch v1.0
    git checkout v1.0
~~~

- merge, push, delete

~~~
    git push origin v1.0
    git checkout master
    git merget v1.0
    git push origin master
    git push origin --delete v1.0
~~~
