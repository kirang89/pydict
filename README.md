## pydict

A simple Python implementation of the CPython dictionary object using Hash Tables.

### Usage Examples

```python
hmap = HashMap()

# You can also give the mappings directly as key value arguments
hmap = HashMap(a='A', b='B', c='C')

# NOTE: Currently only string keys are supported.

# Set/Get/Delete value the same way you would do so in a dictionary. Infact, most
# of the CPython dictionary methods work with HashMap as well.

hmap['d'] = 'D'

aval = hmap['a']

del hmap['d']

```
