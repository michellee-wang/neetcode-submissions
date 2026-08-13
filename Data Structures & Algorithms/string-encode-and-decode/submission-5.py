class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += s + "#%@($)"
        return encoded
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        parts = s.split("#%@($)")
        return parts[:-1]