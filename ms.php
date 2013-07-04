<?php

$data = array(14, 5, 7, 10, 11, 2, 1, 4, 6, 3, 12, 8, 9, 13);
print_r(array('input data: ', $data));
print_r(array('result', divide($data)));

function divide($data) {
    $length = count($data);

    if ($length > 2) {
        $left = array_slice($data, 0, $length / 2);
        $right = array_slice($data, $length / 2);
        return merge(divide($left), divide($right));
    } else {
        return sortData($data);
    }
}

function sortData($data) {
    if (count($data) == 1) {
        return $data;
    }

    return $data[0] < $data[1]
        ? $data
       : array($data[1], $data[0]);
}

function merge($left, $right) {
    $item = array();
    $i=0; $j=0;
    while (count($item) < (count($left) + count($right))) {
        if ($i >= count($left)) {
            $item[] = $right[$j++];
            continue;
        } elseif ($j>=count($right)) {
            $item[] = $left[$i++];
            continue;
        }

        if ($left[$i] < $right[$j]) {
            $item[] = $left[$i++];
        } else {
            $item[] = $right[$j++];
        }
    }

    return $item;
}
