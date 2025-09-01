import sys
cmd=sys.argv[1]
if cmd=="reverse":
  inputPath=sys.argv[2]
  outputPath=sys.argv[3]
  contents=""
  with open(inputPath,"r") as f:
    contents=f.read()
  with open(outputPath,"w") as f:
    f.write(contents[::-1])
elif cmd=="copy":
  contents=""
  inputPath=sys.argv[2]
  outputPath=sys.argv[3]
  with open(inputPath,"r") as f:
    contents=f.read()
  with open(outputPath,"w") as f:
    f.write(contents)
elif cmd=="duplicate-contents":
  inputPath=sys.argv[2]
  n=int(sys.argv[3])
  contents=""
  with open(inputPath,"r") as f:
    contents=f.read()
  with open(inputPath,"w") as f:
    for i in range(n):
      f.write(contents)
elif cmd=="replace-string":
  inputPath=sys.argv[2]
  needle=sys.argv[3]
  newString=sys.argv[4]
  contents=""
  newContents=""
  with open(inputPath,"r") as f:
    contents=f.read()
  newContents=contents.replace(needle,newString)
  with open(inputPath,"w") as f:
    f.write(newContents)
else:
  print("not a valid command")
