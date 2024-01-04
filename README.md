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

### Find in multiple files

```bash
grep -r 'ERROR' # find in current directory
```

```bash
grep -rl 'ERROR' # only show file names
```

```bash
grep -rl --exclude='*.py' ERROR # exclude all .py files
grep -rl --exclude-dir='.git' ERROR # exclude a directory
```

```bash
grep -rl --include='log*' ERROR # include only log files
grep -rl --include-dir='.' ERROR # include a directory
```

```bash
grep -l "DEBUG" **/*(.) # zsh include all files in all directories
```

```bash
find . -type f -iname 'log*' # find all files named 'log*' in current directory, ignore case
```

```bash
find . -not -name 'log*' # find all files not named 'log*'
```

```bash
find . -mtime +7 # find files that were modified more than 7 days back in current directory
```

```bash
find . -size +10k # find files with size greater than 10 kilobytes in current directory
```

```bash
find . -type f -name 'log*' -exec wc -l {} + # count lines of all log* files
```

```bash
find . -type f -name 'log*' -exec mv {} . \;
```



