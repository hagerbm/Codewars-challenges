#include <iostream>
#include <string>
#include <sstream>

// Challenge Description:
// Write a function that takes in a string of one or more words, 
// and returns the same string, but with all five or more letter words 
// reversed (Just like the name of this Kata). Strings passed in will 
// consist of only letters and spaces. Spaces will be included only when 
// more than one word is present.

// Examples:

// spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
// spinWords( "This is a test") => returns "This is a test" 
// spinWords( "This is another test" )=> returns "This is rehtona test"

//  My solution


// Function to reverse words with a length of 5 or more
std::string spinWords(const std::string &str)
{
    std::stringstream ss(str); // Create a stringstream object to read from the input string
    std::string word = ""; // Variable to store each word from the string
    std::string result = ""; // Variable to store the resulting string after reversing words

    // Loop through each word in the stringstream
    while (ss >> word) {
        if (word.length() >= 5) { // Check if the word has a length of 5 or more
            std::reverse(word.begin(), word.end()); // Reverse the word using the std::reverse function
        }
        result += word + " "; // Concatenate the word (reversed if applicable) with a space to the result string
    }

    // Remove the extra space at the end of the result string
    if (!result.empty()) {
        result.pop_back(); // Remove the last character, which is the extra space
    }

    return result; // Return the resulting string with reversed words
}
