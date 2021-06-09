-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 09, 2021 at 06:55 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kaksha`
--

-- --------------------------------------------------------

--
-- Table structure for table `assignment`
--

CREATE TABLE `assignment` (
  `assignment_id` int(11) NOT NULL,
  `assignment_name` varchar(30) DEFAULT NULL,
  `class_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `due_date` datetime DEFAULT NULL,
  `pdf_path` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `assignment`
--

INSERT INTO `assignment` (`assignment_id`, `assignment_name`, `class_id`, `subject_id`, `due_date`, `pdf_path`) VALUES
(1, 'AM_Tutorial_01', 9, 4, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\AM 3\\Tutorial\\D10A_01_Aamir_Ansari (01).pdf'),
(2, 'AM_Tutorial_02', 9, 4, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\AM 3\\Tutorial\\D10A_01_Aamir_Ansari (02).pdf'),
(3, 'AM_Tutorial_03', 9, 4, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\AM 3\\Tutorial\\Tutorial 3.pdf'),
(4, 'AM_Tutorial_04', 9, 4, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\AM 3\\Tutorial\\Tutorial 4.pdf'),
(5, 'DBMS_01', 9, 5, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\DBMS\\Experiment 01\\DBMS Experiment 01.pdf'),
(6, 'DBMS_02', 9, 5, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\DBMS\\Experiment 02\\DBMS Experiment 02.pdf'),
(7, 'DBMS_03', 9, 5, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\DBMS\\Experiment 03\\Lab Assignment 3.pdf'),
(8, 'DBMS_04', 9, 5, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\DBMS\\Experiment 04\\Aamir Ansari - Experiment 04.pdf'),
(9, 'DSA_01', 9, 1, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\DSA\\Experiment 01\\Write-up\\Write up.pdf'),
(10, 'DSA_02', 9, 1, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\DSA\\Experiment 02\\Write-up\\Write-up.pdf'),
(11, 'DSA_03', 9, 1, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\DSA\\Experiment 03\\Write-up\\Write-up.pdf'),
(12, 'DSA_04', 9, 1, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\DSA\\Experiment 04\\Write-up\\Write-up.pdf'),
(13, 'PCOM_01', 9, 6, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\PCOM\\Assignment\\Aamir Ansari - PCOM Assignment 1.pdf'),
(14, 'PCOM_02', 9, 6, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\PCOM\\Assignment\\Aamir Ansari - PCOM Assignment 2.pdf'),
(15, 'PCOM_03', 9, 6, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\PCOM\\Assignment\\Aamir-Ansari_PCOM-Assignment-03.pdf'),
(16, 'PCOM_04', 9, 6, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\PCOM\\Assignment\\Aamir-Ansari_PCOM-Assignment-04.pdf'),
(17, 'PCOM_05', 9, 6, '2021-05-22 17:41:33', 'E:\\Sem-3\\LabWork - Assignments\\PCOM\\Assignment\\Aamir-Ansari_PCOM-Assignment-05.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `branch`
--

CREATE TABLE `branch` (
  `branch_id` int(11) NOT NULL,
  `branch_name` varchar(20) DEFAULT NULL,
  `branch_fullname` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `branch`
--

INSERT INTO `branch` (`branch_id`, `branch_name`, `branch_fullname`) VALUES
(1, 'ETRX', 'Electronics'),
(2, 'CMPN', 'Computers'),
(3, 'INST', 'Instrumentation'),
(4, 'EXTC', 'Electronics and Telecommunication'),
(5, 'INFT', 'Information Technology');

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `class_id` int(11) NOT NULL,
  `division` varchar(3) NOT NULL,
  `semester` tinyint(4) DEFAULT NULL,
  `branch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`class_id`, `division`, `semester`, `branch_id`) VALUES
(9, 'A', 3, 5),
(10, 'B', 3, 5),
(11, 'A', 4, 5),
(12, 'B', 4, 5),
(13, 'A', 3, 2),
(14, 'B', 3, 2),
(15, 'A', 4, 2),
(16, 'B', 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `exam`
--

CREATE TABLE `exam` (
  `exam_id` int(11) NOT NULL,
  `exam_name` varchar(20) DEFAULT NULL,
  `subject_id` int(11) NOT NULL,
  `exam_date` datetime DEFAULT NULL,
  `exam_fullname` varchar(100) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `exam`
--

INSERT INTO `exam` (`exam_id`, `exam_name`, `subject_id`, `exam_date`, `exam_fullname`, `class_id`) VALUES
(1, 'IA-1', 1, '0000-00-00 00:00:00', 'Internal Assesment Test 1', 9),
(2, 'IA-1', 2, '0000-00-00 00:00:00', 'Internal Assesment Test 1', 9),
(3, 'IA-1', 3, '0000-00-00 00:00:00', 'Internal Assesment Test 1', 9),
(4, 'IA-1', 4, '0000-00-00 00:00:00', 'Internal Assesment Test 1', 9),
(5, 'IA-1', 5, '0000-00-00 00:00:00', 'Internal Assesment Test 1', 9),
(6, 'IA-1', 6, '0000-00-00 00:00:00', 'Internal Assesment Test 1', 9),
(7, 'IA-2', 1, '0000-00-00 00:00:00', 'Internal Assesment Test 2', 9),
(8, 'IA-2', 2, '0000-00-00 00:00:00', 'Internal Assesment Test 2', 9),
(9, 'IA-2', 3, '0000-00-00 00:00:00', 'Internal Assesment Test 2', 9),
(10, 'IA-2', 4, '0000-00-00 00:00:00', 'Internal Assesment Test 2', 9),
(11, 'IA-2', 5, '0000-00-00 00:00:00', 'Internal Assesment Test 2', 9),
(12, 'IA-2', 6, '0000-00-00 00:00:00', 'Internal Assesment Test 2', 9);

-- --------------------------------------------------------

--
-- Table structure for table `exam_timetable`
--

CREATE TABLE `exam_timetable` (
  `exam_timetable_id` int(11) NOT NULL,
  `exam_timetable_title` varchar(30) DEFAULT NULL,
  `exam_timetable_description` varchar(100) DEFAULT NULL,
  `exam_timetable_photo` blob DEFAULT NULL,
  `class_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `notes`
--

CREATE TABLE `notes` (
  `notes_id` int(11) NOT NULL,
  `notes_name` varchar(30) DEFAULT NULL,
  `notes_pdf` varchar(1000) DEFAULT NULL,
  `class_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `notes`
--

INSERT INTO `notes` (`notes_id`, `notes_name`, `notes_pdf`, `class_id`, `subject_id`) VALUES
(3, 'DSA', 'E:\\Sem-3\\Data_Structures\\C_and_Data_Structures_-_Balaguruswamy.pdf', 9, 1),
(4, 'PCPF', 'E:\\Sem-3\\PCPF\\Programming_Language_Pragmatics_3rd_Edition.pdf', 9, 2),
(5, 'OOPM', 'E:\\Sem-3\\OOPM\\java_programming_from_the_ground_up.pdf', 9, 3),
(7, 'DBMS', 'E:\\Sem-3\\DBMS\\Database Management Systems (DBMS).pdf', 9, 5),
(15, 'AM_3', 'E:/Sem-3/AM 3/APPLIED MATHEMATICS III By G.V. KUMBHOJKAR- By EasyEngineering.net.pdf', 9, 1),
(18, 'AM_3.1', '', 9, 1),
(19, 'AM_3.2', 'E:/Sem-3/AM 3/APPLIED MATHEMATICS III By G.V. KUMBHOJKAR- By EasyEngineering.net.pdf', 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `notice`
--

CREATE TABLE `notice` (
  `notice_id` int(11) NOT NULL,
  `notice_title` varchar(100) DEFAULT NULL,
  `notice_description` varchar(1000) DEFAULT NULL,
  `class_id` int(11) NOT NULL,
  `type` smallint(6) DEFAULT NULL,
  `photo_path` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `notice`
--

INSERT INTO `notice` (`notice_id`, `notice_title`, `notice_description`, `class_id`, `type`, `photo_path`) VALUES
(7, 'Time Table', NULL, 9, 1, 'E:\\KAKSHA\\resources\\timetable\\tt.png'),
(8, 'UTSAV\'21', 'Everyone note that, on account of Utsav\' 21, 11&12 th May, 2021, will be non instructional days.', 9, 2, NULL),
(10, 'CN extra lecture', 'There will be extra lecture of CN on 15 may, at 3:00 pm', 9, 2, NULL),
(12, 'MahaDBT Portal Date extended till 28th May 2021', 'Students those whose Application are reverted from college Login for Correction.', 9, 2, NULL),
(13, 'Submission of OS Lab assignments 08', 'Submission of Lab assignment of OS experiment 08 is extended to saturday (30/05/2021)', 9, 2, NULL),
(24, 'Python Viva', 'Python viva will be conducted on 22nd may', 9, 2, NULL),
(27, 'Some ttilte', 'Some description', 9, 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `result_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `marks` float DEFAULT 0,
  `out_of` float DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`result_id`, `student_id`, `exam_id`, `marks`, `out_of`) VALUES
(1, 1, 1, 19, 20),
(2, 1, 2, 18, 20),
(3, 1, 3, 8, 20),
(4, 1, 4, 12, 20),
(5, 1, 5, 4, 20),
(6, 1, 6, 13, 20),
(7, 1, 7, 18, 20),
(8, 1, 8, 20, 20),
(9, 1, 9, 1, 20),
(10, 1, 10, 17, 20),
(11, 1, 11, 6, 20),
(12, 1, 12, 13, 20),
(37, 2, 1, 20, 20),
(38, 2, 2, 13, 20),
(39, 2, 3, 18, 20),
(40, 2, 4, 1, 20),
(41, 2, 5, 17, 20),
(42, 2, 6, 9, 20),
(43, 2, 7, 5, 20),
(44, 2, 8, 16, 20),
(45, 2, 9, 12, 20),
(46, 2, 10, 19, 20),
(47, 2, 11, 15, 20),
(48, 2, 12, 16, 20),
(113, 3, 1, 12, 20),
(114, 3, 2, 18, 20),
(115, 3, 3, 20, 20),
(116, 3, 4, 20, 20),
(117, 3, 5, 20, 20),
(118, 3, 6, 14, 20);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `role_id` int(11) NOT NULL,
  `roles_description` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`role_id`, `roles_description`) VALUES
(1, 'CR'),
(2, 'Student'),
(3, 'Class-Teacher'),
(4, 'Teacher'),
(5, 'Lab-Incharge');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL,
  `f_name` varchar(20) DEFAULT NULL,
  `l_name` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_no` varchar(15) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `branch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `f_name`, `l_name`, `email`, `phone_no`, `pin`, `gender`, `branch_id`) VALUES
(1, 'Pooja', 'Shetty', 'pooja.shetty@ves.ac.in', '9876543210', '123', 'F', 5),
(2, 'Charusheela', 'Nehte', 'charusheela.nehete@ves.ac.in', '9876543210', '123', 'F', 5),
(3, 'Vidya', 'pujari', 'vidya.pujari@ves.ac.in', '9876543210', '123', 'F', 5),
(4, 'Sandeep', 'Utala', 'sandeep.utala@ves.ac.in', '9876543210', '123', 'M', 5),
(5, 'Ravi', 'Shankar', 'ravi.shankar@ves.ac.in', '9876543210', '123', 'M', 5),
(6, 'Manoj', 'Sabnis', 'manoj.sabnis@ves.ac.in', '9876543210', '123', 'M', 5),
(7, 'Dimple', 'Bohra', 'dimple.bohra@ves.ac.in', '9876543210', '123', 'F', 5),
(8, 'Chintan', 'Jethva', 'chintan.jethva@ves.ac.in', '9876543210', '123', 'M', 5),
(9, 'Vinita', 'Mishra', 'vinita.mishra@ves.ac.in', '9876543210', '123', 'F', 5),
(10, 'Sukanya', 'Roychaudry', 'sukanya.r@ves.ac.in', '9876543210', '123', 'F', 5);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL,
  `roll_no` tinyint(4) DEFAULT NULL,
  `f_name` varchar(20) DEFAULT NULL,
  `l_name` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `phone_no` varchar(15) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `roll_no`, `f_name`, `l_name`, `email`, `pin`, `phone_no`, `gender`, `role_id`, `class_id`) VALUES
(1, 1, 'Aamir', 'Ansari', '2019aamir.ansari@ves.ac.in', 'as25414618', '9876543210', 'M', 2, 9),
(2, 15, 'Isha', 'Gawde', '2019isha.gawde@ves.ac.in', '123', '9876543210', 'F', 2, 9),
(3, 30, 'Kanaiya', 'Kanabar', '2019kanaiya.kanabar@ves.ac.in', '123', '9876543210', 'M', 2, 9),
(4, 27, 'Jisha', 'Philip', '2019jisha.philip@ves.ac.in', '123', '9876543210', 'F', 1, 9),
(5, 61, 'VKrishna', 'Subramanian', '2019krishna.v@ves.ac.in', '123', '9876543210', 'M', 2, 9),
(6, 24, 'Sreekesh', 'Iyer', '2019sreekesh.Iyer@ves.ac.in', '123', '9876543210', 'M', 2, 9),
(7, 53, 'Ninad', 'Rao', '2019ninad.rao@ves.ac.in', '123', '9876543210', 'M', 1, 9),
(8, 100, 'Sherlock', 'Holmes', 'a', 'a', '9876543211', NULL, 1, 9),
(9, 99, 'admin', 'admin', 'admin@ves.ac.in', '123', NULL, 'M', 1, 9);

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `subject_id` int(11) NOT NULL,
  `subject_name` varchar(20) DEFAULT NULL,
  `semester` tinyint(4) DEFAULT NULL,
  `branch_id` int(11) NOT NULL,
  `subject_fullname` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`subject_id`, `subject_name`, `semester`, `branch_id`, `subject_fullname`) VALUES
(1, 'DSA', 3, 5, 'Data Structures and Analysis '),
(2, 'PCPF', 3, 5, 'Programming and Fundamentals'),
(3, 'OOPM', 3, 5, 'Object Oriented Programming'),
(4, 'AM_3', 3, 5, 'Engineering Mathematics-III'),
(5, 'DBMS', 3, 5, 'Database Management System'),
(6, 'PCOM', 3, 5, 'Principle of Communication'),
(7, 'COA', 4, 5, 'Computer Organization and Architecture'),
(8, 'Python', 4, 5, 'Python'),
(9, 'AM_4', 4, 5, 'Engineering Mathematics-IV'),
(10, 'AT', 4, 5, 'Automata Theory'),
(11, 'OS', 4, 5, 'Operating Systems'),
(12, 'CNND', 4, 5, 'Computer Network and Network Design');

-- --------------------------------------------------------

--
-- Table structure for table `teaches`
--

CREATE TABLE `teaches` (
  `teaches_id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teaches`
--

INSERT INTO `teaches` (`teaches_id`, `staff_id`, `class_id`, `subject_id`, `role_id`) VALUES
(1, 1, 11, 12, 4),
(2, 2, 11, 10, 4),
(3, 3, 11, 8, 4),
(4, 4, 11, 11, 3),
(5, 5, 11, 9, 4),
(6, 6, 11, 7, 4),
(7, 2, 9, 1, 4),
(8, 5, 9, 4, 4),
(9, 7, 9, 3, 3),
(10, 8, 9, 6, 4),
(11, 10, 9, 5, 4),
(12, 9, 9, 2, 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assignment`
--
ALTER TABLE `assignment`
  ADD PRIMARY KEY (`assignment_id`),
  ADD KEY `class_id` (`class_id`),
  ADD KEY `subject_id` (`subject_id`);

--
-- Indexes for table `branch`
--
ALTER TABLE `branch`
  ADD PRIMARY KEY (`branch_id`);

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`class_id`),
  ADD KEY `branch_id` (`branch_id`);

--
-- Indexes for table `exam`
--
ALTER TABLE `exam`
  ADD PRIMARY KEY (`exam_id`),
  ADD KEY `subject_id` (`subject_id`),
  ADD KEY `class_id` (`class_id`);

--
-- Indexes for table `exam_timetable`
--
ALTER TABLE `exam_timetable`
  ADD PRIMARY KEY (`exam_timetable_id`),
  ADD KEY `class_id` (`class_id`);

--
-- Indexes for table `notes`
--
ALTER TABLE `notes`
  ADD PRIMARY KEY (`notes_id`),
  ADD KEY `class_id` (`class_id`),
  ADD KEY `subject_id` (`subject_id`);

--
-- Indexes for table `notice`
--
ALTER TABLE `notice`
  ADD PRIMARY KEY (`notice_id`),
  ADD KEY `class_id` (`class_id`);

--
-- Indexes for table `result`
--
ALTER TABLE `result`
  ADD PRIMARY KEY (`result_id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `exam_id` (`exam_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_id`),
  ADD KEY `branch_id` (`branch_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`),
  ADD KEY `role_id` (`role_id`),
  ADD KEY `class_id` (`class_id`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`subject_id`),
  ADD KEY `branch_id` (`branch_id`);

--
-- Indexes for table `teaches`
--
ALTER TABLE `teaches`
  ADD PRIMARY KEY (`teaches_id`),
  ADD KEY `staff_id` (`staff_id`),
  ADD KEY `class_id` (`class_id`),
  ADD KEY `subject_id` (`subject_id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assignment`
--
ALTER TABLE `assignment`
  MODIFY `assignment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `branch`
--
ALTER TABLE `branch`
  MODIFY `branch_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `class_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `exam`
--
ALTER TABLE `exam`
  MODIFY `exam_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `exam_timetable`
--
ALTER TABLE `exam_timetable`
  MODIFY `exam_timetable_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notes`
--
ALTER TABLE `notes`
  MODIFY `notes_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `notice`
--
ALTER TABLE `notice`
  MODIFY `notice_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `result`
--
ALTER TABLE `result`
  MODIFY `result_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=119;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `subject`
--
ALTER TABLE `subject`
  MODIFY `subject_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `teaches`
--
ALTER TABLE `teaches`
  MODIFY `teaches_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `assignment`
--
ALTER TABLE `assignment`
  ADD CONSTRAINT `assignment_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`),
  ADD CONSTRAINT `assignment_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`);

--
-- Constraints for table `class`
--
ALTER TABLE `class`
  ADD CONSTRAINT `class_ibfk_1` FOREIGN KEY (`branch_id`) REFERENCES `branch` (`branch_id`);

--
-- Constraints for table `exam`
--
ALTER TABLE `exam`
  ADD CONSTRAINT `exam_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`),
  ADD CONSTRAINT `exam_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`);

--
-- Constraints for table `exam_timetable`
--
ALTER TABLE `exam_timetable`
  ADD CONSTRAINT `exam_timetable_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`);

--
-- Constraints for table `notes`
--
ALTER TABLE `notes`
  ADD CONSTRAINT `notes_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`),
  ADD CONSTRAINT `notes_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`);

--
-- Constraints for table `notice`
--
ALTER TABLE `notice`
  ADD CONSTRAINT `notice_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`);

--
-- Constraints for table `result`
--
ALTER TABLE `result`
  ADD CONSTRAINT `result_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),
  ADD CONSTRAINT `result_ibfk_2` FOREIGN KEY (`exam_id`) REFERENCES `exam` (`exam_id`);

--
-- Constraints for table `staff`
--
ALTER TABLE `staff`
  ADD CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`branch_id`) REFERENCES `branch` (`branch_id`);

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`),
  ADD CONSTRAINT `student_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`);

--
-- Constraints for table `subject`
--
ALTER TABLE `subject`
  ADD CONSTRAINT `subject_ibfk_1` FOREIGN KEY (`branch_id`) REFERENCES `branch` (`branch_id`);

--
-- Constraints for table `teaches`
--
ALTER TABLE `teaches`
  ADD CONSTRAINT `teaches_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`staff_id`),
  ADD CONSTRAINT `teaches_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`),
  ADD CONSTRAINT `teaches_ibfk_3` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`),
  ADD CONSTRAINT `teaches_ibfk_4` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
