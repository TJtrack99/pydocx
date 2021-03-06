**0.4.3**

- Allow a file-like object to be passed into the DocXParser constructor.
- Added basic support for footnotes.

**0.4.2**

- Fixed a problem with calculating image sizes

**0.4.01**

- Take into account run position and size to apply superscript and subscript
  tags to runs that would look like they have superscript and subscript tags
  but are being faked due to positioning and sizing.

**0.4.00**

- External images are now handled. This causes a backwards incompatible change
  with all handers related to images.

**0.3.23**

- Added support for style basedOn property

**0.3.22**

- Fixed a bug in which the run paragraph mark properties were used as run
  properties (pPr > rPr within a style definition)
- Fixed a bug in which the run paragraph properties defined a global style
  identifier, any of those styles defined globally were ignored.
- Fixed a bug which allowed run properties to reference paragraph properties,
  and paragraph properties to reference run properties. Such instances are now
  ignored.

**0.3.21**

- We are once again supporting files that are missing images.

**0.3.20**

- Fixed a problem with list nesting. We were marking list items as the first list item in error.

**0.3.19**

- Added support for python 3.3
- Fixed a problem with list nesting with nested sublists that have the same ilvl.

**0.3.18**

- Fixed an issue with marking runs as underline when they were not supposed to be.

**0.3.17**

- Fixed path issue on Windows for Zip archives
- Fixed attribute typo when attempting to generate an error message for a missing required resource

**0.3.16**

- CHANGELOG.md was missing from the MANIFEST in 0.3.15 which would cause the setup to fail.

**0.3.15**

- Use inline span to define styles instead of div
- Use ems for HTML widths instead of pixels
- If a property value is ``off``, it is now considered disabled

**0.3.14**

- Use paths from ``_rels/.rels`` instead of hardcoding

**0.3.13**

- Significant performance gains for documents with a large number of table cells.
- Significant performance gains for large documents.

**0.3.12**

- Added command line support to convert from docx to either html or markdown.

**0.3.11**

- The non breaking hyphen tag was not correctly being imported. This issue
  has been fixed.

**0.3.10**

- Found and optimized a fairly large performance issue with tables that had large amounts of content within a single cell, which includes nested tables.

**0.3.9**

- We are now respecting the ``<w:tab/>`` element.
  We are putting a space in everywhere they happen.
- Each styling can have a default defined based on values in ``styles.xml``.
  These default styles can be overwritten using the ``rPr`` on the actual ``r`` tag.
  These default styles defined in ``styles.xml`` are actually being respected now.

**0.3.8**

- If zipfile fails to open the passed in file,
  we are now raising
  ``MalformedDocxException``
  instead of
  ``BadZipFIle``.

**0.3.7**

- Some inline tags
  (most notably the underline tag)
  could have a ``val`` of ``none``
  and that would signify that the style is disabled.
  A ``val`` of ``none`` is now correctly handled.

**0.3.6**

- It is possible for a docx file to not contain a ``numbering.xml`` file
  but still try to use lists.
  Now if this happens all lists get converted to paragraphs.

**0.3.5**

- Not all docx files contain a ``styles.xml`` file.
  We are no longer assuming they do.

**0.3.4**

- It is possible for ``w:t`` tags to have ``text`` set to ``None``.
  This no longer causes an error when escaping that text.

**0.3.3**

- In the event that ``cElementTree`` has a problem parsing the document,
  a ``MalformedDocxException`` is raised
  instead of a
  ``SyntaxError``

**0.3.2**

- We were not taking into account that vertical merges should have a continue attribute,
  but sometimes they do not,
  and in those cases word assumes the continue attribute.
  We updated the parser to handle the cases in which the continue attribute is not there.
- We now correctly handle documents with unicode character in the namespace.
- In rare cases,
  some text would be output with a style when it should not have been.
  This issue has been fixed.

**0.3.1**

- Added support for several more OOXML tags including:

  - caps
  - smallCaps
  - strike
  - dstrike
  - vanish
  - webHidden

More details in the README.

**0.3.0**

- We switched from using
  stock ``xml.etree.ElementTree`` to
  using ``xml.etree.cElementTree``.
  This has resulted in a fairly significant speed increase for python 2.6
- It is now possible to create your own pre processor to do additional pre processing.
- Superscripts and subscripts are now extracted correctly.

**0.2.1**

- Added a changelog
- Added the version in ``pydocx.__init__``
- Fixed an issue with duplicating content if there was indentation or justification on a p element that had multiple t tags.
