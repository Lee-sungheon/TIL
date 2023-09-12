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



