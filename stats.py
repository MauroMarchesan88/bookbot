def get_char_count (contents):
  str_int = {}
  for index, char in enumerate(contents):
    if char.lower() in str_int:
      str_int[char.lower()] += 1
    else:
      str_int[char.lower()] = 1
  return str_int

def sort_on (items):
  return items["num"]

def pretty_sort(file_contents):
  base = get_char_count(file_contents)
  new_list = []
  for k in base:
    if k.isalpha():
      new_list.append({"char": k, "num": base[k]})
  new_list.sort(reverse=True, key=sort_on)
  for item in new_list:
    print(f"{item["char"]}: {item["num"]}")

def get_num_words (path):
  with open(path) as f:
    file_contents = f.read()
    amount_of_strs =  len(file_contents.split())
  return f"Found {amount_of_strs} total words", file_contents
