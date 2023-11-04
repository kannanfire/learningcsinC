package main

import (
	"fmt"
	"os"
	"strconv"
	"sys"

	// "golang.org/x/sys/unix"
)

const (
	FIONREAD = 0x541B
)

func open_pid(pid int) (int, error) {
	r1, _, err := sys.Syscall(sys.Syscall.sys_pidfd_open, uintptr(pid), 0, 0)

	if err != 0 {
		return -1, err
	}

	return int(r1), nil
}

// func steal_fd(pidfd, targetfd int) (int, error) {
// 	r1, _, error
// }

func main() {
	var (
		pid, fd int
		err 	error
	)

	pid, err = strconv.Atoi(os.Args[1])
	fd, err = strconv.Atoi(os.Args[2])

	pidfd, err = open_pid(pid)

	if err != nil {
		panic(err)
	}

	fmt.Printf("pid: %d\n",pidfd)
}