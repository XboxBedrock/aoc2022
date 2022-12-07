require "luarocks.loader"
local inspect = require('inspect')

function string.starts(String,Start)
  return string.sub(String,1,string.len(Start))==Start
end

function string.split(inputstr, sep)
  if sep == nil then
     sep = "%s"
  end
  local t={}
  for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
     table.insert(t, str)
  end
  return t
end

function noop()
  return 0
end

local tot = 0
local hirarchy = {}
local cwd = {}
local cwdfor = {}
local lines = {}
local size = {}
for line in io.lines() do
  table.insert(lines, line)
end

for idx, line in ipairs(lines) do
  if (string.starts(line, "$ cd"))
  then
    local dumb = string.split(line, " ")[3]
    if (dumb == "..")
    then
      table.remove(cwd)
    else
      table.insert(cwd, dumb)
      table.insert(cwdfor, table.concat(cwd, "+"))
    end
  elseif (string.starts(line, "$ ls")) 
  then
    noop()
  else 
    local tot = ""
    for idx, dir in ipairs(cwd) do
        if idx ~= 1 then tot = tot .. '+' end
        tot = tot .. dir
        if (string.starts(line, "dir") == false) then
          if (size[tot] == nil) then
            size[tot] = 0
          end
          size[tot] = size[tot] + tonumber(string.split(line, " ")[1])
        end
    end
  end
end

local atot = 70000000 - size['/']

for idx, cnt in pairs(size) do
  if (atot + cnt) >= 30000000 then
    if (atot - cnt) < tot then
      tot = cnt
    end
  end
end

print(tot)