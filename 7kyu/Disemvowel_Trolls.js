/* Challenge Description:
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, 
neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.

*/

// Solution #1
function disemvowel(str) {
  return str.replace(/[aeiou]/gi, '')
}

// Solution #2

function isCharacterALetter(char) {
  return /[a-zA-Z]/.test(char)
}
function isVowel(x) {
  var result
  x = x.toUpperCase()
  result = x == 'A' || x == 'E' || x == 'I' || x == 'O' || x == 'U'
  return result
}
function disemvowel(str) {
  var result = ''
  if (str.length > 1) {
    for (const char of str) {
      if (isCharacterALetter(char) && isVowel(char)) {
        continue
      } else {
        result += char
      }
    }
  }
  console.log('str: ' + str + '\nresult: ' + result)
  return result
}
