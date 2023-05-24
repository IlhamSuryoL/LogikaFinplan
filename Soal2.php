<?php
function carikata($text) {
    $carikata = array('sang gajah', 'serigala', 'harimau');
    $result = array();

    foreach ($carikata as $kata) {
        $count = substr_count($text, $kata);
        $result = array_merge($result, array_fill(0, $count, $kata));
    }

    $output = implode(' - ', $result);
    return $output;
}
$inputText = "Berikut adalah kisah sang gajah. Sang gajah memiliki teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah.";
$outputText = carikata($inputText);
echo $outputText;

?>