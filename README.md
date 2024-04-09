# all-about-log
## It can be used to Practice
* cat
* less/more
* head/tail
* grep
* sed
* awk
* sort
* uniq
* diff
* vim
* or more ...

## The log file should contain

* one line log should contain
  * timestamp
  * log level
    * LOG.DEBUG
    * LOG.ERROR
  * file name
  * function name
  * line number
  * info
* json stuff
  * nest json
  * some errors in json
* empty lines

## Tasks

### Find "ERROR"

```shell
grep "ERROR" log
```

```shell
grep -i "error" log # case-insensitive
```

```shell
grep -n "ERROR" log # along with line number
```
```shell
grep -c "ERROR" log # total lines
```
```shell
grep "ERROR" log | less # if the output is very large
```

```shell
grep -v "ERROR" log # the opposite
```

```shell
sed -n '/ERROR/p' log
```

```shell
sed -n '/ErroR/Ip' log | wc -l # total lines, case-insensitive
```

```shell
awk '/ERROR/' log
```

```shell
awk 'tolower($0) ~ /error/' log # case-insensitive
```

### Find "ERROR" or "DEBUG"

```shell
grep -e "ERROR" -e "DEBUG" log
```

```shell
grep -E "ERROR|DEBUG" log
```

```shell
grep -e "ERROR" -e "DEBUG" log | sort -k 3 # sort by log level
```

```shell
sed -n '/ERROR/p; /DEBUG/p' log
```

```shell
awk '/ERROR/ || /DBUG/' log
```

### Find  "ERROR" in "a.cpp"

```shell
grep "ERROR" log | grep "a.cpp"
```

```shell
sed -n "/ERROR/{/a.cpp/p;}" log
```

```shell
awk '/ERROR/ && /a.cpp/' log
```

### Find all file names containing 'ERROR'

```shell
grep "ERROR" log | grep -o "[a-z]*.cpp" | sort | uniq
```

### Find how many "ERROR" in each file

```shell
grep "ERROR" log | grep -io "[a-z]*.cpp" | sort | uniq -c | sort -nr
```

### Find  all "ERROR" that appeared between 19:00:00 and 24:00:00

```shell
grep -E '(19|2[0-3]):..:.. \[ERROR\]' log
```

```shell
grep -E '(19|2[0-3]):..:.. \[ERROR\]' log | sort -k2,2 # sort by time
```

```shell
sed -n '/19:00:00/,/24:59:59/{/\[ERROR\]/p;}' log
```

```shell
sed -n '/19:00:00/,/24:59:59/{/\[ERROR\]/p;}' log | sort -k2.4,2.5 -k2.1,2.2 # sort by minute, then hour
```

```shell
awk '/(19|2[0-3]):..:.. \[ERROR\]/' log
```

### Find all lines start/end with 2023-12-20

```shell
grep '^2023-12-20' log
grep '2023-12-20$' log
```

```shell
sed -n '/^2023-12-20/' log
sed -n '/2023-12-20$/' log
```

```shell
awk '/^2023-12-20/{ print $0 }' log
awk '/2023-12-20$/{ print $0 }' log
```

### Find in multiple files

```shell
grep -r 'ERROR' # find in current directory
```

```shell
grep -rl 'ERROR' # only show file names
```

```shell
grep -rl --exclude='*.py' ERROR # exclude all .py files
grep -rl --exclude-dir='.git' ERROR # exclude a directory
```

```shell
grep -rl --include='log*' ERROR # include only log files
grep -rl --include-dir='.' ERROR # include a directory
```

```shell
grep -l "DEBUG" **/*(.) # zsh include all files in all directories
```

```shell
find . -type f -iname 'log*' # find all files named 'log*' in current directory, ignore case
```

```shell
find . -not -name 'log*' # find all files not named 'log*'
```

```shell
find . -mtime +7 # find files that were modified more than 7 days back in current directory
```

```shell
find . -size +10k # find files with size greater than 10 kilobytes in current directory
```

```shell
find . -type f -name 'log*' -exec wc -l {} + # count lines of all log* files
```

```shell
find . -type f -name 'log*' -exec mv {} . \;
```



