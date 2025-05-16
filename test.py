from typing import List

def hIndex(citations: List[int]) -> int:
        # one more for 0 citation
        citation_papers = [0] * (len(citations) + 1)
        for citation in citations:
            citation_papers[min(len(citations), citation)] += 1
            print(citation_papers)

        CP = 0
        for H_idx in range(len(citation_papers) - 1, -1, -1):
            CP += citation_papers[H_idx]
            if (CP >= H_idx):
                return H_idx
            

print(hIndex([3, 0, 6, 1, 5]))