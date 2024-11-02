#!bin/bash


get_size(){
    local path="$1"
    local size=$(du -hs "$path" 2>/dev/null | cut -f1)
    echo $size
}

items=$(ls -A)

for item in $items; do
    size=$(get_size "$item")
#    echo -e $size"\t"$item
    result+=("$size $item")
done # | sort -rh -k1,1

printf "%s\n" "${result[@]}" | sort -rh | column -t