exports.charCount = function(string) {
    //object to log characters and their count
    countObj = {};
    //taking the string to lower, filter out all but alpha characters
    const charArray = string.toLowerCase().split('').filter(element => element.match(/[a-zA-Z]/));
    //looping through array and logging character count into the object
    for (let i = 0; i < charArray.length; i++) {
        if(countObj[charArray[i]]) {
            countObj[charArray[i]] += 1;
        } else {
            countObj[charArray[i]] = 1;
        }
    }
    //creating answer array by dumping object entries, then running sort function against it
    const ansArray = Object.entries(countObj).sort((a, b) => {
       //sorting by count in descending order
        if (a[1] > b[1]) {return -1};
        if (a[1] < b[1]) {return 1};
        //if count matches then sort alphabetically in ascending order
        if (a[1] === b[1]) {
            if(a > b) {return 1};
            if(a < b) {return -1};
        }

    });
    //returning the sorted answer array
    return ansArray;

};

