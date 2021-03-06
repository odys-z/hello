
# About

Hello Mocha - webpack TDD support without running Node.

See [VITALIY ZAKHAROV, Unit Testing With Webpack & Mocha](https://www.threatstack.com/blog/unit-testing-with-webpack-mocha)

# Quick Start

install Webpack

```
npm install --save-dev webpack
```

install Mocha and dependencies

```
npm install webpack-node-externals --save-dev
npm install --save-dev mocha chai mocha-webpack
npm install --save-dev babel-preset-es2015
npm install --save-dev webpack-shell-plugin
```

create a spec

```
touch spec-helper.js
```

run test (TODO webpack config needing fixed)

```
webpack -config webpack-test.config.js # ignore the server error
npm test
```

## Debug with [Karma](https://developers.google.com/web/updates/2017/06/headless-karma-mocha-chai)

```
    npm i --save-dev karma karma-chrome-launcher karma-mocha karma-chai
    npm i --save-dev karma-webpack
```

## More readings and references

- [TeejayVanSlyke, How to set up a test runner for modern JavaScript using Webpack, Mocha, and Chai](http://teejayvanslyke.com/how-to-set-up-a-test-runner-for-modern-javascript.html)

- [VITALIY ZAKHAROV, Unit Testing With Webpack & Mocha](https://www.threatstack.com/blog/unit-testing-with-webpack-mocha)

- [Andy Haskell, webpack: From 0 to automated testing](https://itnext.io/webpack-from-0-to-automated-testing-4634844d5c3c)

- A helpful diagram for understanding
[test run cycle overview from Mocha doc](https://mochajs.org/#run-cycle-overview)

- [chai-stats Assert API](https://www.chaijs.com/api/assert/)

# Your first test case

see test/test-target.case.js

Also note the test configuration:

- Test entries for webpack is provided in test/all-tests.js

- which in turn specify that all files ended with '.case.js' will be tested.

```
import {TargetClass, TargetFunc} from '../src/target.js';
import { expect } from 'chai';
var assert = require('assert');

describe('tests sample target', function() {
  let clssTarget, funcTarget
  before(function() {
	clssTarget = new TargetClass();
  });

  it('test funcA()', function() {
	assert.equal('ok', clssTarget.funcA('hi'));
  });
});
```

## using chai-stats

To assert number almost equals, we need [chai-stats](https://www.chaijs.com/plugins/chai-stats/).

```
    npm install chai-stats
```

in test-case.js

```
import chai from 'chai'
import { expect, assert } from 'chai'
import chaiStats from 'chai-stats'

before(function() {
		chai.use(chaiStats);
	});
```

Tip: not this

```
import {chaiStats} from 'chai-stats'
```
# TODO

We need a browser environment to run tests.

https://developers.google.com/web/updates/2017/06/headless-karma-mocha-chai

# Troubleshooting

- Chunk.parents

```
WEBPACK  Failed to compile with 1 error(s)
Error: Chunk.parents: Use ChunkGroup.getParents() instead
```

It's probably a bug:

see [here](https://github.com/GoogleChromeLabs/preload-webpack-plugin/issues/60),
also [here](https://github.com/zinserjan/mocha-webpack/issues/304)

```
npm i mocha-webpack@next
```

- server error

```
events.js: 167
    throw error; // Unhandled 'error' event
    ^
```

Avoid start Node server.

Try this:

Remove webpack onBuildExit plugin, which is calling mocha. Then in test scripts,
call webpack first.

```
    "test": "webpack --config webpack-test.config.js && mocha-webpack --webpack-config webpack-test.config.js \"spec/**/*.spec.js\" || true"
```
