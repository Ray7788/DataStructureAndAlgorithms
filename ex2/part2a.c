#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
	if (argc < 1) {
		//not enough command-line parameters
		printf("Error: expected some command-line parameters\n");
		return 0;
	}

	int maxLen = 0; // length of the longest string
	int maxIndex = 0; // //index of longest string

	if (argv == NULL) {
		printf("Null array is invalid");	//will not work for null arrays
		return 0;
	}
	else {
		if (argc == 1) {
			printf("Empty list");
		}
		else {
			for (int i = 1; i < argc; i++) {
				if (strlen(argv[i]) > maxLen) {
					maxLen = strlen(argv[i]);
					maxIndex = i;
				}
			}
			printf("%s\n", argv[maxIndex]);
		}
	}

	return 0;
}