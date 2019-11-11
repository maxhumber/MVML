import os
import shutil

os.remove('mummify/mummify.log')
os.remove('mummify/model.pkl')
os.remove('mummify/.gitignore')
os.remove('mummify/.git')
shutil.rmtree('mummify/.mummify')
