#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>

int main(int argc, char *argv[], char *envp[]) {
  fprintf(stdout, "1 OUT: argvc %d, argv0 %s argv1 %s argv2 %s\n",
      argc, argv[0], argv[1], argv[2]);

  pid_t pid = fork();
  pid_t xpid;
  int pidstatus;

  if (pid < 0) {
    perror("2 fork");
    exit(EXIT_FAILURE);
  }

  fprintf(stdout, "3 OUT Hey yo, this is the %d process\n", pid);
  fprintf(stderr, "4 ERR Hey yo, this is the %d process\n", pid);

  if (pid == 0) {
    fprintf(stdout, "5 OUT now this is the child, %d\n", pid);
    fprintf(stderr, "6 ERR Hey yo, this is the %d process\n", pid);
    fclose(stdout);
    fprintf(stdout, "7 OUT Does this appear?\n");

    int fd = open("AK", O_RDWR|O_CREAT|O_TRUNC, S_IRUSR|S_IWUSR|S_IRWXO|S_IRWXG);
    fprintf(stderr, "8 ERR File descripritor, %d, is this stdout?", fd);
    stdout = fdopen(fd, "w");
    fprintf(stdout, "8A OUT IS THIS STDOUT NOW?\n");
    argv[0] = argv[1];
    execve(argv[0], argv, envp);
  }

  fprintf(stdout, "9 OUT PARENT HERE\n");
  fprintf(stderr, "A ERR PARENT WHINING\n");
  sleep(30);
  xpid = wait(&pidstatus);
  fprintf(stdout, "B OUT pid %d exit w/status %08x\n", xpid, pidstatus);
  exit(EXIT_SUCCESS);
}	
