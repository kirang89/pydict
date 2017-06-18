## pydict

A simple Python implementation mimicking CPython dictionary using Hash Tables.

### Usage Examples

```python
d = Dictionary()

# You can also give the mappings directly as key value arguments
d = Dictionary(a='A', b='B', c='C')

# NOTE: Currently only string keys are supported.

# Set/Get/Delete value the same way you would do so in a dictionary. Infact, most
# of the CPython dictionary methods work with Dictionary as well.

d['d'] = 'D'

aval = d['a']

del d['d']

```
