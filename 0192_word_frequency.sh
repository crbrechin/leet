# Read from the file words.txt and output the word frequency list to stdout.
for word in $(cat words.txt); do echo $word; done | sort | uniq -c | awk '{print $2 " " $1}' | sort -k2nr
