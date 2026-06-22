func characterReplacement(s string, k int) int {
    start := 0
    end := 0
	maxCount := 0
	maxLength := 0
	count := make(map[byte]int)
	while end < len(s) {
		count[s[end]]++
		maxCount = max(maxCount, count[s[end]])
		if end - start + 1 - maxCount > k {
			count[s[start]]--
			start++
		}
		maxLength = max(maxLength, end - start + 1)
		end++
	}
	return maxLength
}
