The 9th Age XML Rulebook
========================

[![Build Status](https://travis-ci.org/redelmann/ninth-age-xml.svg?branch=master)](https://travis-ci.org/redelmann/ninth-age-xml)

This project is an effort to port [the 9th Age rulebook][rulebook] to an appropriately annotated XML file.
The goal is to provide tool creators with a richly annotated and easily usable version of the rulebook.

Contributing
============

All contributions to the XML file are welcomed!
Before you submit your modifications, please ensure that the XML file still follows the DTD.
To check this, you can for instance use `xmllint`:

```
xmllint --valid --noout rulebook.xml
```

I am of course open to changes in the DTD itself. Please be sure to motivate your changes! 

License
=======

This work is a derivative work of the 9th Age project.

Please see the [license of the 9th Age][license] for more details.

[license]: http://www.the-ninth-age.com/license.html
[rulebook]: http://www.the-ninth-age.com/index.php?simple-page/