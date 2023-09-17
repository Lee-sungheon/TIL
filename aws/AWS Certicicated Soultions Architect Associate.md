# AWS Certificated Solutions Architect Associate

**AWS 자격증 Udemy 강의 요약** 



# Section 04. IAM

### IAM Section 

- IAM: Idenitity and Access Management => 글로벌 서비스
- 루트 계정
  - 기본으로 생성
  - 오직 계정을 생성할 때만 사용되어야 하며, 그 후에는 루트 계정을 더 이상 사용해서도, 공유해서도 안됨
- 사용자 생성
  - 하나의 사용자는 조직 내의 한 사람에 해당
  - 필요하다면 사용자들을 그룹으로 묶을 수 있음
- 그룹
  - 그룹에는 사용자만 배치할 수 있으며, 다른 그룹을 포함시킬 순 없음
  - 하나의 사용자가 다수의 그룹에 속할 수도 있음
- IAM: Permission
  - 사용자 또는 그룹에게 정책, 또는 IAM이라고 불리는 JSON 문서를 지정할 수 있음
  - 이 정책들을 사용해 사용자들의 권한을 정의할 수 있게 됨
  - AWS에서는 모든 사용자에게 모든 권한을 허용하지 않음 => 보안 문제 및 비용 문제
  - 최소 권한의 원칙을 적용
    - 사용자가 꼭 필요로 하는 것 이상의 권한을 주지 않음



### IAM Policies

- IAM Pocicies Structure

  - 구성 요소

    - Version: 정책 언어 버전, 항상 '2012-10-17'이 포함
    - Id: 정책을 식별하는 ID (optional)
    - Statement: 한개 이상의 문장 (required)

  - Statement의 구성 요소

    - Sid: 문장 ID로 문장의 식별자 (optional)
    - 효과(Effect): 문장이 특정 API에 접근하는걸 허용할지 거부할지에 대한 내용 (Allow / Deny)
    - 원칙(Principal): 특정 정책이 적용될 사용자, 계정, 혹은 역할로 구성
    - 조치(Action): effect에 기반해 허용 및 거부되는 API 호출의 목록
    - 리소스(Resource): 적용될 action의 리소스 목록
    - 컨디션(Condition): statement가 언제 적용될지를 결정 (optional)

    ```json
    {
      "Version": "2012-10-17",
      "Id": "S3-Account-Permissions",
      "Statememt": [
        {
          "Sid": "1",
          "Effect": "Allow",
          "Pricipal": {
            "AWS": ["arn:aws:iam:123456789012:root"]
          },
          "Action": [
            "s3:GetObject",
            "s3:PutObject"
          ],
          "Resource": ["arn:aws:s3::mybucket/*"]
        }
      ]
    }
    ```



### IAM MFA

- Password Policy
  - Strong passwords = 계정의 보안을 높여줌
  - AWS password policy 세팅 방법
    - 비밀번호 최소 길이 설정
    - 특정 유형의 글자 사용 요구
    - IAM 사용자들의 비밀번호 변경 허용 및 금지
    - 일정 기간이 지나면 새 비밀번호 설정 요구
    - 사용자의 비밀번호 재사용을 막기
- MFA (Multi Factor Authentication)
  - 유저들은 AWS 계정에 접근할 수 있고 리소스들을 변경하고 삭제할 수도 있으므로 이 위험에서 계정을 보호해야함
  - MFA = password you know + security device you own
- AWS에서 MFA 장치 옵션
  - 가상 MFA 장치 (Virtual MFA device)
    - Google Authenticator (phone only)
    - Authy (multi- device)
    - 하나의 장치에서 여러 계정 및 사용자를 지원함
  - 범용 두 번째 인자 보안 키 (U2F - Universion 2nd Factor Security Key)
    - 물리적 장치
    - Yubico(AWS 제3자 회사) 의 YubiKey
    - 하나의 보안 키로 여러 루트 계정과 IAM 유저를 지원
  - 하드웨어 키 팝 MFA 장치 (Hardware Key Fob MFA Device)
    - 물리적 장치
    - Gemalto(AWS 제3자 회사)
  - 하드웨어 키 팝 MFA 장치 (미국 정부 AWS GovCloud 전용)
    - SurePassID(AWS 제3자 회사)



### AWS 엑세스 키, CLI 및 SDK

- 유저가 AWS에 접근하는 방법
  - AWS Management Console (protected by password + MFA)
  - AWS Command Line Interface (CLI): protected by access keys
  - AWS Software Developer Kit (SDK): for code -> protected by access keys
- 액세스 키 생성 방법
  - AWS Console을 사용해서 생성할 수 있음
  - 사용자들이 자신들의 액세스 키를 직접 관리
  - 액세스 키는 비밀번호와 마찬가지로 암호와 같음 
  - 액세스 키는 절대 공유 되면 안됨
  - Access Key ID ~= username
  - Secret Access Key ~= password
- AWS CLI
  - 명령줄 셀에서 명령어를 사용하여 AWS 서비스들과 상호작용할 수 있도록 해 주는 도구
  - 모든 명령어가 aws로 시작
  - CLI를 사용하면 AWS 서비스의 공용 API로 직접 액세스가 가능
  - CLI를 통해 리소스를 관리하는 스크립트 개발해 일부 작업을 자동화할 수 있음
- AWS SDK
  - 소프트웨어 개발 키트
  - 특정 언어로 된 라이브러리의 집합 => 프로그래밍 언어에 따라 개별 SDK가 존재
  - SDK를 사용하면 AWS 서비스의 공용 API로 직접 액세스가 가능
  - 터미널을 통한 접근이 아니라 코딩을 통해 애플리케이션 내에 심어두는 방식
  - 다양한 프로그래밍 언어 지원 (JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js, C++)
  - 모바일 SDKs (Android, iOS, ...)
  - IoT Device SDKs (Embedded C, Ariduino, ...)
  - 예시: AWS CLI는 파이썬 AWS SDK로 구성 돼 있음



### AWS 클라우드쉘

- 특정 지역에서만 가능
- AWS 클라우드에서 무료로 사용 가능한 터미널같은 개념
- 장점
  - CLI를 사용할 때 API 호출을 반환 
    - --region 을 이용해 API 호출을 할 리전을 지정할 수도 있음
    - 클라우드쉘에서 기본 리전은 현재 로그인 된 리전
  - 전체 저장소가 있음
  - 구성이 가능
    - 글씨 크기, 테마 선택, 안전하게 붙여넣기 기능
    - 파일 업로드 및 다운로드 가능
    - 탭 구성 가능



### AWS 서비스에 대한 IAM Role

- AWS 서비스 몇 가지는 우리의 계정에서 실행해야 하며, 이를 위해서는 사용자와 마찬가지로 어떤 권한이 필요함
- IAM Role은 사용자와 같지만 실제 사람이 사용하도록 만들어진 것이 아니고 AWS 서비스에 의해 사용되도록 만들어짐



### IAM 보안 도구

- IAM 자격 증명 보고서(Credentials Report)
  - 계정 수준(account- level)에서 가능
  - 보고서는 계정에 있는 사용자와 다양한 자격 증명의 상태를 포함
- IAM 액세스 관리자(Access Adviser)
  - 사용자 수준(user-level)에서 가능
  - 사용자에게 부여된 서비스의 권한과 해당 서비스에 마지막으로 엑세스한 시간이 보임
  - 해당 도구를 사용하여 어떤 권한이 사용되지 않는지 볼 수 있고 따라서 사용자의 권한을 줄여 최소권한의 원칙을 지킬 수 있음



## Section 05. EC2 기초

### EC2 기초

- EC2(Elastic Compute Cloud): AWS에서 제공하는 서비스형 인프라스트럭처
- 포함하고 있는 서비스
  - 가상 머신 임대 (EC2) => EC2 인스턴스
  - 데이터를 가상 드라이브 또는 EBS 볼륨에 저장 (EBS)
  - 엘라스틱 로드 밸런서로 로드를 분산 (ELB)
  - 오토 스케일링 그룹을 통해 서비스를 확장(ASG)
- EC2의 사용법을 아는 것은 클라우드 작동 방식을 이해할 때 필수적
- EC2 사이징(Sizing) & 설정 옵션(configuration options)
  - Operating System (OS): Linux, Windows or Mac OS
  - CPU: 컴퓨티 성능과 코어의 양
  - RAM: 램덤 엑세스 메모리의 양
  - 용량 공간
    - 네트워크를 통해 연결할 스토리지 필요 여부 (EBS & EFS)
    - 하드웨어 (EC2 인스턴스 스토어)
  - 네트워크 카드: 속도가 빠른 카드, 어떤 종류의 공용 IP
  - 방화병 규칙: 보안 그룹
  - 부트스트랩 스크립트 (처음에 설정): EC2 사용자 데이터
- EC2 사용자 데이터
  - EC2 사용자 데이터 스크립트를 사용하여 인스턴스를 부트스트래핑할 수 있음
  - 부트스트래핑: 머신이 작동될 때 명령을 시작하는 것
  - 스크립트는 처음 시작할 때 한 번만 실행됨
  - EC2 사용자 데이터가 자동화하는 작업들
    - 업데이트
    - 소프트웨어 설치
    - 일반적인 파일들을 인터넷에서 다운로드
    - 우리가 생각하는 모든 것들
  - EC2 사용자 데이터 스크립트는 루트 계정에서 실행 => 모든 명령문은 sudo로 해야 함
- EC2 인스턴스를 재실행시, 사설 IP는 항상 같은 상태로 유지되지만 공용 IP는 변경될 수 있음



### EC2 인스턴스 유형 기본 사항

- EC2 인스턴스 유형 - 개요
  - https://aws.amazon.com/ec2/instance-types/
  - m5.2xlarge 의미
    - m: 인스턴스 클래스
    - 5: 인스턴스의 세대(generation)
    - 2xlarge: 인스턴스 클래스의 사이즈 => 크기가 클수록 더 높은 메모리와 CPU 개수를 가짐
- 범용 인스턴스
  - 웹 서버나 코드 저장소와 같은 다양한 작업에 적합
  - 컴퓨팅, 메모리, 네트워킹 간의 균형도 잘 맞음
  - t2.micro 도 범용 인스턴스
- 컴퓨팅 최적화 인스턴스
  - 컴퓨터 집약적인 작업에 최적화된 인스턴스
  - 사용 사례
    - 일부 데이터의 일괄 처리
    - 미디어 트랜스코딩 작업 시
    - 고성능 웹 서버가 필요할 때
    - 고성능 컴퓨팅이라는 HPC 작업을 할 때
    - 과학적 모델링 & 머신 러닝
    - 전용 게임 서버
  -  Computing을 나타내는 C로 시작하는 이름을 가지고 있음
- 메모리 최적화 인스턴스
  - 메모리에서 대규모 데이터셋을 처리하는 유형에 빠른 성능을 제공
  - 사용 사례
    - 고성능의 관계형 / 비관계형 데이터베이스
    - 분산 웹스케일 캐시 저장소
    - BI(business intelligence)에 최적화된 인 메모리 데이터베이스
    - 대규모 비정형 데이터의 실시간 처리를 실행하는 애플리케이션
  - 보통 Ram을 나타내는 R로 시작하는 이름을 가지고 있음 (X1 이나 대용량 메모리, Z1도 있음)
- 스토리지 최적화 인스턴스
  - 로컬 스토리지에서 대규모의 데이터셋에 엑세스할 때 적합한 인스턴스
  - 사용 사례
    - 고주파 온라인 트랜잭션 처리(OLTP) 시스템
    - 관계형 & NoSQL 데이터베이스
    - 메모리 데이터베이스의 캐시 (ex - Redis)
    - 데이터 웨어하우징 애플리케이션
    - 분산 파일 시스템
  - I, G, H1으로 시작하는 이름을 가지고 있음

- 인스턴스 정보 보는 사이트: https://www.ec2instances.info/



### 보안 그룹 및 클래식 포트 개요

- 보안 그룹 개요
  - 보안 그룹은 AWS 클라우드에서 네트워크 보안을 실행하는데 핵심이 됨
  - EC2 인스턴스에 들어오고 나가는 트래픽을 제어
  - 보안 그룹은 오직 허용 규칙만 포함함
  - 보안 그룹 또는 IP 주소를 참조해 규칙을 만들 수 있음

- 보안 그룹 딥 다이브
  - 보안 그룹은 EC2 인스턴스의 방화벽
  - 규제 목록
    - 포트로의 엑세스 통제
    - 인증된 IP 주소의 범위를 확인해 IPv4인지 IPv6인지 확인
    - 외부에서 인스턴스로 들어오는 인바운드 네트워크 통제
    - 인스턴스에서 외부로 나가는 아웃바운드 네트워크 통제
  - 타입, 프로토콜, 포트 범위, 소스, 설명으로 구성
- 보안 그룹에 대해 알아야 하는 것 
  - 여러 인스턴스에 연결할 수 있음 => 보안 그룹과 인스턴스 간의 일대일 관계는 없음
  - 보안 그룹은 지역과 VPC 결합으로 통제되어 있음
  - 보안 그룹은 EC2 외부에 있음 => 트래픽이 차단되면 EC2 인스턴스는 확인할 수 없음
  - SSH 액세스를 위해 하나의 별도 보안 그룹을 유지하는 것이 좋음
  - 타임아웃으로 애플리케이션에 접근할 수 없으면 보안 그룹의 문제
  - 어떤 포트에 연결을 시도하는데 컴퓨터가 계속 멈추고 대기하기만 한다면 보안 그룹의 문제
  - ''연결 거부'' 오류가 발생하면 보안 그룹은 실행됐고 트래픽은 통과했지만 애플리케이션에 문제가 생겼거나 실행되지 않은 등 문제가 발생한 것
  - 기본적으로 모든 인바운드 트래픽은 차단되어 있고, 모든 아웃바운드 트래픽은 허용되어 있음
- 알아야 하는 포트
  - 22번 포트 => SSH(Secure Shell): Linux에서 EC2 인스턴스로 로그인하도록 함
  - 21번 포트 => FPT(File Transfer Protocol): 파일 공유 시스템에 파일을 업로드하는데 사용
  - 22번 포트 => SFTP (Secure FIle Transfer Protocol): SSH를 통해서 전송되고 보안 파일 전송 프로토콜이 되기 때문에 22번 포트를 사용함
  - 80번 포트 => HTTP: 보안이 되지 않은 사이트에 액세스하기 위함
  - 443번 포트 => HTTPS: 보안이 된 사이트에 엑세스하기 위함
  - 3389 포트 => RDP (Remote Desktop Protocol): 윈도우 인스턴스에 로그인할 때 사용



### 
