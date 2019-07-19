Mem=(`free -h | grep "Mem" | awk '{print $2,$3,$4,$5,$6,$7}'`)
text="*Time-state*
---------------------------------------------------
Time: `date`
Uptime: `uptime`
---------------------------------------------------
*CPU-state*
---------------------------------------------------
The system CPU is `echo "100-$(vmstat 1 5 | sed -n '3,$p' | awk '{x = x + $15} END {print x/5}' | awk -F. '{print $1}')" | bc`%
---------------------------------------------------
*Memory-state*
---------------------------------------------------
Total:          $Mem[1]
Used:           $Mem[2]
Free:           $Mem[3]
Shared:         $Mem[4]
Buff/Cache:     $Mem[5]
Available:      $Mem[6]
---------------------------------------------------
*Disk-state*
---------------------------------------------------
`df -h | grep "Filesystem" | awk '{print $1,$2,$3,$5}'`
`df -h | grep "/dev/vda1" | awk '{print $1,$2,$3,$5}'`
---------------------------------------------------
*V2ray-state*
---------------------------------------------------
`/usr/sbin/service v2ray status | sed -n '3,4p' | sed 's/^[ \t]*//g'`
"
curl -k --data chat_id=$1 --data "text=$text" --data "parse_mode=Markdown" "https://api.telegram.org/botxxxxxxxxx:XXXXXXXXXXXXXXXXXXXXXXX/sendMessage"