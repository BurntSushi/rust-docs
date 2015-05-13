This is an internal meta package that burntsushi uses to generate documentation
for all of his crates. It is not on `crates.io`. The only purpose of this crate
is to generate docs.

This repo isn't directly shareable, but it might serve as a useful model for
you to copy and tweak. Namely, all I do is run the `update` script in the
repository's root directory.

`update` is responsible for updating the `Cargo.lock` file, generating the
docs, patching the index with only the crates I want to show and then uploading
the docs to my web server.

Finally, I have these rules in my `nginx.conf`:

```nginx
location =/rustdoc/ {
    rewrite ^/rustdoc/$ /rustdoc/docs/ permanent;
}

location /rustdoc {
    root /home/andrew/www/burntsushi.net;
    autoindex on;
}
```

The first redirects `/rustdoc` to `/rustdoc/docs`, where `docs` is the name of
*this* crate.

If you want to use this, you'll need to tweak `Cargo.toml`, `update` and
`patch-index.py`. The first and last files contain the crates you want to show.
`update` probably has some custom shell utilities from my `~/bin` that you
don't have.
