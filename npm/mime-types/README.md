# About

Convert mime type to and from document type.

Reference:

[W3cubDocs/http](https://docs.w3cub.com/http/basics_of_http/mime_types/complete_list_of_mime_types)

## Credits

Source modified from [jshttp/mime-types](https://github.com/jshttp/mime-types)

## Why?

Because it's worth to try without Node.js dependency.

See [#50](https://github.com/jshttp/mime-types/issues/50#issuecomment-442916069)

# Qick start

install

```
    npm install mime-types-no-node
```

test

```
    npm install
	npm test
```

Testing code snippet:

```
    it('mime2type', () => {
        assert.equal(Mime.extension('image/png;base64'), 'png', '1 png');
    });

    it('type2mime', () => {
        assert.equal(Mime.lookup('png'), 'image/png', '00.2 --png');
	});
```
