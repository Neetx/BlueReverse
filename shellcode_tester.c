#include<unistd.h>
#include<sys/mman.h>

unsigned char output[] = ""; //put shellcode here

int main(){

	mprotect((void*)((intptr_t)output & ~0xFFF), 8192, PROT_READ|PROT_EXEC);

	int (*ret)();
	ret =(int(*)())output;
	(int)(*ret)();
}

